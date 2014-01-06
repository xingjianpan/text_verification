# Convert pdf to txt
#pdf2txt.py -t text S1-Source.pdf >S1-Source_txt.txt



#deal with unicode write

In [70]: for each in t:
    f.write(each.encode('utf8’))



tree = etree.parse("doc/test.xml”)
root =  tree.getroot() 
root.xpath('//text()’)
 
 


In [163]: for el in root.iter():                                       
             print ("%s - %s" % (el.tag,el.text)) 

for el in root.iter():
    if el.text is not None and el.tag[-1]=='t':
        print("%s - %s" %(el.tag, el.text)) 





page2=parse('S1-Target.html').getroot() 

for el in page2.iter():
    print("%s - %s" %(el.tag, el.text))
    
       
for el in page2.iter():
    if el.text is not None:
        print("%s - %s" %(el.tag, el.text))   
        
        
page3=parse('S1-Target.xml').getroot() 

for el in page3.iter():
    print("%s - %s" %(el.tag, el.text))
    
       
for el in page3.iter():
    if el.text is not None:
        print("%s - %s" %(el.tag, el.text))
    
    

for el in page.iter():
    if el.text is not None:
        print("%s - %s" %(el.tag, el.text)) 
        
                
for el in page2.iter():
    if el.text is not None:
        print("%s - %s" %(el.tag, el.text))           
        

for el in page3.iter():
    if el.text is not None:
        print("%s - %s" %(el.tag, el.text))


#read a1.txt and convert to comparabale format a1_.txt
#in this case, a1.txt is text converted from pdfminder
f=open('a1.txt','U')

f=open('a1.txt','U').readlines()

fs=''.join(f)
fs=' '.join(fs.split())

import textwrap

ft=textwrap.wrap(fs,width=40)

fs_='\n'.join(ft)

f2=open('a1_.txt','w')
f2.write(fs_)

f2.close()


#read a2.txt and convert to comparabale format a2_.txt
#in this case a2.txt is conveted from html using lxml



def convert_xml_to_string(xml_file):
    """
    input:xml file
    output: string
    """
    from lxml import etree
    tree = etree.parse(xml_file)
    root = tree.getroot() 
    for element in root.iter():
        text_list = []
        text_list.append(el.text)
    res = ''.join(text_list)
    return res
        
    
def convert_html_to_string(html_file):
    """
    input:html file
    output: string
    """
    from lxml.html import parse
    page=parse(html_file).getroot()
    for el in page.iter():
        text_list = []
        text_list.append(el.text)
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
    return out

       
       
       
       
        
f=open('a2.txt','U')

f=open('a2.txt','U').readlines()

fs=''.join(f)
fs=' '.join(fs.split())

import textwrap

ft=textwrap.wrap(fs,width=40)

fs_='\n'.join(ft)

f2=open('a2_.txt','w')
f2.write(fs_)

f2.close()
        