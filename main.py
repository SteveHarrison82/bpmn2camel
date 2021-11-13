import os
import unittest


#from bpmn_process import bpmn2json
from bpmn_process.bpmn2json import BpmnXml2py


class B2JsoonConvertertest(unittest.TestCase):
    sample_xml = "./bpmn/mybpmn.xml"
    xml2py = None
    result = None

    def test_bpmn2json(self):
        bpmnxml2py = BpmnXml2py()
        bpmnxml2py.load_bpmnxml2py("mybpmn2.xml")
        #bpmnxml2py.load_bpmnxml2py(os.path.abspath(self.sample_xml))
        print (bpmnxml2py.bpmnxml2py)
        self.xml2py = bpmnxml2py.bpmnxml2py
        bpmnxml2py.get_processes(self.xml2py)
        bpmnxml2py.generate_json()


if __name__ == '__main__':
    unittest.main()
