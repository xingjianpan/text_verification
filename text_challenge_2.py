# -*- coding: utf-8 -*-  
#TODO
#PDF can compare with xml
#html can compare with html
#

 
 
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
    tmp  = ''.join(text.split())
    return tmp


def join_list_together(list):
    list = [line for line in mystr.split('\n') if line.strip() != ''] 


def remove_extra_blank_lines(text):
    list = [line for line in text.split('\n') if line.strip() != ''] 
    return '\n'.join(list)
    
def re_format_text(text):
    s1 = replace_line_breaks_with_space(text)
    s2 = replace_tabs_with_space(s1)
    s3 = remove_extra_space_within_sentence(s2)
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
            print 'cannot write to file, trying encoding without using utf8'
            # try:
            #     f.write(string)
            #     print 'Done'
            # except:
            #     print 'cannot write to file. program will exit'


#to delete
    
    
def format_string(string):
    """
    input:string
    output:string
    width - 40
    compress spaces in string
    """   
    #import textwrap
    #break string into sentences,output is list
    #sentences = find_sentense(string)
    tmp  = string.replace("\r","\n").replace("\r\n","\n").replace("\r\t"," ").replace("\t"," ").strip()
    tmp2 = ''.join(tmp.split('\n'))
    sentences = splitParagraphIntoSentences(tmp2)
    clean_sentences = [cleaner(sentense) for sentense in sentences]
    #join the list back into a string
    #new_string = ' '.join(string.split())    
    #wrapped_new_string_in_list=textwrap.wrap(new_string,width=100)
    #wrapped_new_string = '\n'.join(wrapped_new_string_in_list)
    res = '\n'.join(clean_sentences)
    res2 = comprese_tab(res)
    #return wrapped_new_string
    return res2

def comprese_tab(string):
    temp = string.split('\t')
    res = ''.join(temp)
    return res     

def cleaner(sentense):
    cleaned_sentense = sentense.replace("\r","\n").replace("\r\n","\n").replace("\r\t"," ").replace("\t"," ").strip()
    return cleaned_sentense

       
      
      


 
def remove_html_comment(string):
    import re
    output = re.sub(r"<!--(.*?)-->", r'', string)
    #pattern=re.complie(r"<!--(.*?)-->")
    #pattern.sub('', string)
    return output
    
        
pdf_s=re_format_text(convert_pdf_to_string('S7-Source.pdf'))
html_s=re_format_text(convert_html_to_string('S6-Source.html'))    
html_t=re_format_text(convert_html_to_string('S6-Target.html'))
xml_t=re_format_text(convert_xml_to_string('S6-Target.xml'))
write_string_to_file(pdf_s,'pdf_s.txt')
write_string_to_file(html_s,'html_s.txt')
write_string_to_file(html_t,'html_t.txt')
write_string_to_file(xml_t,'xml_t.txt')

python diff.py pdf_s.txt html_t.txt -m > res_pdf_html_1.html
python diff.py pdf_s.txt xml_t.txt -m > res_pdf_xml_2.html
python diff.py html_s.txt xml_t.txt -m > res_html_xml_3.html
python diff.py html_s.txt html_t.txt -m > res_html_html_4.html
