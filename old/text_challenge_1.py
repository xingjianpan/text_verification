def convert_pdf_to_string(pdf_file):
    """
    input:pdf file
    output:string
    """
    import subprocess
    #s=subprocess.Popen('pdf2txt.py S1-Source.pdf',stdout=subprocess.PIPE,shell=True)
    #s=subprocess.Popen(['pdf2txt.py', 'S1-Source.pdf'],stdout=subprocess.PIPE)
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
    text_list = []
    for element in page.iter():
        if element.text is not None:
            text_list.append(element.text)
    res = ''.join(text_list)
    return res
    


def format_string(string):
    """
    input:string
    output:string
    width - 40
    compress spaces in string
    """   
    import textwrap
    new_string = ' '.join(string.split())    
    wrapped_new_string_in_list=textwrap.wrap(new_string,width=40)
    wrapped_new_string = '\n'.join(wrapped_new_string_in_list)
    return wrapped_new_string
     



       
      
      
def write_string_to_file(string, filename):
    if not string:
        raise 'no string provided'
    if not filename:
        raise 'please input filename'
    with open(filename, 'w') as f:
        try:
            f.write(string)
            print 'Done'
        except:
            print 'cannot write to file, trying encoding using utf8'
            try:
                f.write(string.encode('utf8'))
                print 'Done'
            except:
                print 'cannot write to file. program will exit'

        
pdf_s=format_string(convert_pdf_to_string('S2-Source.pdf'))
html_s=format_string(convert_html_to_string('S2-Source.html'))    
html_t=format_string(convert_html_to_string('S2-Target.html'))
xml_t=format_string(convert_xml_to_string('S2-Target.xml'))
write_string_to_file(pdf_s,'pdf_s.txt')
write_string_to_file(html_s,'html_s.txt')
write_string_to_file(html_t,'html_t.txt')
write_string_to_file(xml_t,'xml_t.txt')

python diff.py pdf_s.txt html_t.txt -m > res_pdf_html.html
python diff.py pdf_s.txt xml_t.txt -m > res_pdf_xml.html

