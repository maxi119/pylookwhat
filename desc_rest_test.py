from docutils import core
from docutils.writers.html4css1 import Writer,HTMLTranslator

class HTMLFragmentTranslator( HTMLTranslator ):
    def __init__( self, document ):
        HTMLTranslator.__init__( self, document )
        self.head_prefix = ['','','','','']
        self.body_prefix = []
        self.body_suffix = []
        self.stylesheet = []
    def astext(self):
        return ''.join(self.body)

html_fragment_writer = Writer()
html_fragment_writer.translator_class = HTMLFragmentTranslator

def reST_to_html( s ):
    return core.publish_string( s, writer = html_fragment_writer )


if __name__ == '__main__':
    fname = "Readme.txt"
    oname = "Readme.html"
    inContent = open( fname, "r").read()
    outContent = reST_to_html( inContent )
    fout = open( oname, "w" )
    fout.write( outContent )
    fout.close()
