# -*- coding: utf-8 -*-
#TODO - enable program to read form a from to get the start and end points for comparision.



#TODO test
def convert_txt_to_string(txt_file):
    import codecs
    with codecs.open(txt_file, 'U',"utf-8") as f:
        content = f.readlines()
        return ''.join(content)

def convert_pdf_to_string(pdf_file):
    """
    input:pdf file
    output:string
    format:same as pdf file
    """
    import subprocess
    #s=subprocess.Popen('pdf2txt.py S1-Source.pdf',stdout=subprocess.PIPE,shell=True)
    #s=subprocess.Popen(['pdf2txt.py', 'S1-Source.pdf'],stdout=subprocess.PIPE
    s=subprocess.Popen(['pdf2txt.py', pdf_file],stdout=subprocess.PIPE)
    out, err = s.communicate()
    #res = ''.join(out.split("\r\n")) #remove "\r\n"
    #res2 = ''.join(out.split("\n"))  #remove "\n"
    try:
        unicode_out = out.decode('utf8')
        return unicode_out
    except:
        return out

def convert_xml_to_string(xml_file):
    """
    input:xml file
    output: string
    """
    from lxml import etree
    tree = etree.parse(xml_file)
    root = tree.getroot()
    text_list = []
    for element in root.iter():
        if element.text is not None:
            if (element.tag[-1] in ['t','p'] or element.tag[-4:] in ['span']) : #'t' and 'span' contains real text
                text_list.append(element.text)
    res = ''.join(text_list)
    return res

def convert_html_to_string(html_file):
    """
    input:html file
    output: string
    """
    from lxml.html import parse
    page=parse(html_file).getroot()
    #content_list = page.xpath("/html/body/text()")
    #text_list = []
    #for element in page.iter():
    #    if element.text is not None:
    #        text_list.append(element.text)
    #res = ''.join(content_list)
    res = page.body.text_content()
    return res

def replace_line_breaks_with_space(text):
    tmp  = text.replace("\n"," ").replace("\r"," ").replace("\r\n"," ")
    return tmp

def replace_tabs_with_space(text):
    tmp  = text.replace("\r\t"," ").replace("\t"," ")
    return tmp

def remove_extra_space_within_sentence(text):
    tmp  = ' '.join(text.split())
    return tmp

def remove_all_space_within_sentence(text):
    tmp  = ''.join(text.split())
    return tmp

def splitParagraphIntoSentences(paragraph):
    ''' break a paragraph into sentences
        and return a list

        after break, there should be no ,.!? sign
        in each sentence.

        note: this basically also means ,.!? are excluded
        from comparasion effectively. If the solution
        request strict comparasion of text including
        these signs, this program will not work
        '''
    import re
    # to split by multile characters

    #   regular expressions are easiest (and fastest)
    sentenceEnders = re.compile('[,.!?]') #add comma
    sentenceList = sentenceEnders.split(paragraph)
    return '\n'.join(sentenceList)

def remove_extra_blank_lines(text):
    list = [line for line in text.split('\n') if line.strip() != '']
    return '\n'.join(list)

def re_format_text(text):
    s1 = replace_line_breaks_with_space(text)
    s2 = replace_tabs_with_space(s1)
    s3 = remove_all_space_within_sentence(s2)
    s4 = splitParagraphIntoSentences(s3)
    s5 = remove_extra_blank_lines(s4)
    return s5

def write_string_to_file(string, filename):
    import codecs
    if not string:
        raise 'no string provided'
    if not filename:
        raise 'please input filename'
    with codecs.open(filename, 'w',"utf-8") as f:
        try:
            #f.write(string.encode('utf8'))
            f.write(string)
            print 'Done'
        except:
            print 'cannot write to file'

def cut_it(text, mark):
    pos = text.find(mark)
    if pos>0:
        text = text[pos:]
    else:
        text = text
    return text

def find_between(s, first, last=None):
    try:
        start = s.index(first)
        if last is None:
            end = len(s)
        else:
            end = s.index(last,start) + len(last)
        return s[start:end]
    except ValueError:
        return""

#TODO test
def judge_file_format(file):
    import os
    file_name = os.path.basename(file)
    if file_name.lower().endswith('.txt'):
        return 'txt'
    elif file_name.lower().endswith('.pdf'):
        return 'pdf'
    elif file_name.lower().endswith('.xml'):
        return 'xml'
    elif file_name.lower().endswith('.html'):
        return 'html'
    else:
        return 'unsupported'

def generate_file_for_comparision(file):
    file_format = judge_file_format(file)
    print file_format
    if file_format == 'txt':
        content = re_format_text(convert_txt_to_string(file))
        write_string_to_file(content ,'COMPARE_txt_file.txt')
        return 'COMPARE_html_file.txt'
    elif file_format == 'pdf':
        content = re_format_text(convert_pdf_to_string(file))
        write_string_to_file(content,'COMPARE_pdf_file.txt')
        return 'COMPARE_PDF_file.txt'
    elif file_format == 'xml':
        content = re_format_text(convert_xml_to_string(file))
        write_string_to_file(content,'COMPARE_xml_file.txt')
        return 'COMPARE_xml_file.txt'
    elif file_format == 'html':
        content = re_format_text(convert_html_to_string(file))
        write_string_to_file(content,'COMPARE_html_file.txt')
        return 'COMPARE_html_file.txt'
    elif file_format == 'unsupported':
        print 'unsupported file format'
        raise
    else:
        print 'not a file'


def generate_comparasion_report(fromfile, tofile):
    import difflib
    import time
    lines = 5

    #fromdate = time.ctime(os.stat(fromfile).st_mtime)
    #todate = time.ctime(os.stat(tofile).st_mtime)
    fromlines = open(fromfile, 'U').readlines()
    tolines = open(tofile, 'U').readlines()
    diff = difflib.HtmlDiff().make_file(fromlines, tolines, fromfile,
                                        tofile, numlines = lines)
    sys.stdout.writelines(diff)


#TODO TEST
def perform_comparision(file1, file2):
    file1 = generate_file_for_comparision(file1)
    file2 = generate_file_for_comparision(file2)
    generate_comparasion_report(file1, file2)

if __name__ == '__main__':
    import sys, os
    for each in sys.argv:
        print each
    #if len(sys.argv) <> 3:
    #    print 'Need two files for comparision.'
    #    sys.exit()
    #else:
    #    perform_comparision(sys.argv[1],sys.argv[2])
    file1 = os.path.abspath(sys.argv[1])
    file2 = os.path.abspath(sys.argv[2])
    perform_comparision(file1, file2)






"""
for manual comparasion and check

txt_s = re_format_text(convert_txt_to_string('background.txt'))
txt_t = re_format_text(convert_txt_to_string('background2.txt'))
pdf_s=re_format_text(convert_pdf_to_string('background.pdf'))
html_s=re_format_text(convert_html_to_string('S1-Source.html'))
html_t=re_format_text(convert_html_to_string('S1-Target.html'))
xml_t=re_format_text(convert_xml_to_string('S1-Target.xml'))
write_string_to_file(txt_s,'txt_s.txt')
write_string_to_file(txt_t,'txt_t.txt')
write_string_to_file(pdf_s,'pdf_s.txt')
write_string_to_file(html_s,'html_s.txt')
write_string_to_file(html_t,'html_t.txt')
write_string_to_file(xml_t,'xml_t.txt')


python diff.py txt_s.txt txt_t.txt -m > res_txt_txt_6.html
python diff.py txt_s.txt pdf_s.txt -m > res_txt_pdf_5.html
python diff.py pdf_s.txt html_t.txt -m > res_pdf_html_1.html
python diff.py pdf_s.txt xml_t.txt -m > res_pdf_xml_2.html
python diff.py html_s.txt xml_t.txt -m > res_html_xml_3.html
python diff.py html_s.txt html_t.txt -m > res_html_html_4.html


pdf_s=find_between(re_format_text(convert_pdf_to_string('S6-Source.pdf')),'DECREE')
html_s=find_between(re_format_text(convert_html_to_string('S6-Source.html')),'DECREE')
html_t=find_between(re_format_text(convert_html_to_string('S6-Target.html')),'DECREE')
xml_t=find_between(re_format_text(convert_xml_to_string('S6-Target.xml')),'DECREE')
write_string_to_file(pdf_s,'pdf_s.txt')
write_string_to_file(html_s,'html_s.txt')
write_string_to_file(html_t,'html_t.txt')
write_string_to_file(xml_t,'xml_t.txt')
"""
