import db.Basic_Latin
import db.Cyrillic
import db.Latin1_Supplement

GLYPHS = (
            db.Basic_Latin.GLYPHS | 
            db.Latin1_Supplement.GLYPHS |
            db.Cyrillic.GLYPHS
        )