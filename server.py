import xmlrpc.server
import xml.etree.ElementTree as ET

class NotebookServer:
    def __init__(self):
        self.database = ET.parse(r'C:\Users\tomaa\PycharmProjects\DistSystAssignment2\notes.xml')

    def add_note(self, topic, text, timestamp):
        #constructs an XML element, note, with two sub-elements note_text and note_timestamp
        #it the nappends these to the note element
        root = self.database.getroot()
        note = ET.Element('note', {'topic': topic})
        noteText = ET.Element('text')
        noteText.text = text
        noteTimestamp = ET.Element('timestamp')
        noteTimestamp.text = timestamp
        note.append(noteText)
        note.append(noteTimestamp)
        ok = False

        # If the root element of the XML tree is empty, a new topic element with a name attribute
        # set to topic is created. The note element is then appended as a child of this new topic
        # element, and the topic element is appended as a child of the root element.
        if len(root) == 0:
            topicElement= ET.Element('topic', {'name': topic})
            topicElement.append(note)
            root.append(topicElement)
        #
        else:
            for i in root:
                if i.attrib['name'] == topic:
                    i.append(note)
                    ok = True
                    break
            if not ok:
                topicElement = ET.Element('topic', {'name': topic})
                topicElement.append(note)
                root.append(topicElement)
        self.database.write('notes.xml')
        return 'Note added'

    def get_notes(self, topic):
        root = self.database.getroot()
        notes = []
        for i in root:
            if i.attrib.get('name') == topic:
                for j in i:
                    noteTextElement = j.find('text')
                    noteTimestampElement = j.find('timestamp')
                    if noteTextElement is not None and noteTimestampElement is not None:
                        noteText = noteTextElement.text
                        noteTimestamp = noteTimestampElement.text
                        notes.append((noteText, noteTimestamp))
                break
        return notes


with xmlrpc.server.SimpleXMLRPCServer(('localhost', 8000)) as server:
    server.register_instance(NotebookServer())
    print('Server started on port 8000')
    server.serve_forever()

