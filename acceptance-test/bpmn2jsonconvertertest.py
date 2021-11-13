import os
import unittest


#from bpmn_process import bpmn2json
from bpmn_process.bpmn2json import BpmnXml2py



class B2JsoonConvertertest(unittest.TestCase):
    sample_xml = "./bpmn/camunda_xml.bpmn"
    xml2py = None

    def test_bpmn2json(self):
        bpmnxml2py = bpmm2json.BpmnXml2py()
        bpmnxml2py.load_bpmnxml2py(os.path.abspath(self.sample_xml))
        print (bpmnxml2py.bpmnxml2py)
        self.xml2py = bpmnxml2py.bpmnxml2py
        bpmnxml2py.get_processes(self.xml2py)
        bpmnxml2py.generate_json()


if __name__ == '__main__':
    unittest.main()
