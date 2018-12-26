from b2jconverter import BpmnXml2py
import os
import unittest

class B2JsoonConvertertest(unittest.TestCase):

    sample_xml = "./bpmn/camunda_xml.bpmn"
    xml2py = None

    def test_bpmn2json(self):
        bpmnxml2py = BpmnXml2py()
        bpmnxml2py.load_bpmnxml2py(os.path.abspath(self.sample_xml))
        print bpmnxml2py.bpmnxml2py
        self.xml2py = bpmnxml2py.bpmnxml2py
        bpmnxml2py.get_processes(self.xml2py)
        bpmnxml2py.generate_json()


if __name__ == '__main__':
    unittest.main()