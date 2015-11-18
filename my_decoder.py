# -*- coding: utf-8 -*-
__author__ = 'PCPC'
import zlib
import codecs
zip_data = r'''db
..........tO.
.0.~..;Xi..*.!6....4....(...G..M......K..`..}?.}WA&...D.p..........d.d....;..0EV.X..4<_.{@JF.......h#.....9X..(...skH
.R.U.)A../]{..c..C\{..f[...0'.^.._.
+...)......{Ar...z@y9Rn...&"....W?.........H
......
0'''
print(codecs.encode(zip_data,'hex'))
decode_data = zlib.decompress(zip_data, 16 | zlib.MAX_WBITS)

print(decode_data)
