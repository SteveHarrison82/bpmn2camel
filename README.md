# POC: BPMN2CAMEL
Proof of Concept [On Progress] : BPMN2CAMEL

Motivation:

Enterprise integration pattern (EIP) is used to connect end-applications that can talk among themselves with same or different protocols.
While connecting the end-applications, a work-flow is realized. These work-flow are executed by CAMEL-API in java world. CAMEL API is specizialized for realizing all possible EIPs (to connect applications)

To create such CAMEL_ROUTE, an end-user could define/design the connectivity using BPMN. Camunda BPMN modeler is one such modeler that comes in two forms: as desktop app or as web-app.
Once the end-user models onnectivity, then this BPMN-XML generated by moderler has to be converted to CAMEL_ROUTE XML. 

The CAMEL_ROUTE XML can then be fed to CAMEL API. This way, end to end-connectivity between different applications can be realized

In this repository there is a crude attempt to MAP the BPMN_XML to CAMEL_ROUTE XML.

The generated CAMEL_ROUTE XML can be fed to CAMEL-API. 

As CAMEL-API is written  using JAVA-API, configuring CAMEL-API module using an agnositic and programing-language independent DSL, such as CAMEL_ROUTE XML, is therefore a good approach.
