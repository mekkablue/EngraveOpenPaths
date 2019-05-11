# EngraveOpenPaths

This is a plugin for the [Glyphs font editor](http://glyphsapp.com/). It closes open paths on export, so they can be exported. In the processing application, the font needs to be turned into outlines, and opened again. This is useful if you need your shapes to be monolines, e.g., for controlling engraving machines.

### Installation

1. Double click the `EngraveOpenPaths.glyphsFilter` file, confirm the dialog(s) that follow.
2. If you are working with Adobe Illustrator, add the `.scpt` file to the Illustrator AppleScript folder:
	1. Open Script Editor.app
	2. Activate *Script Editor > Preferences > Show Script menu in menu bar*
	3. Close Script Editor.app
	4. Open Adobe Illustrator
	5. In the AppleScript menu in the top right corner of the screen, choose *Open Scripts folder > Open Illustrator Scripts folder*
	6. Put the `.scpt` file there

### Workflow for open-path fonts

1. Add an instance in *Font Info > Instances.*
2. In the instance, add a custom parameter, property *Filter,* and value: `EngraveOpenPaths`.
3. Export to the Adobe Fonts Folder **without overlap removal**, and without hinting.

### License

Copyright 2019 Rainer Erich Scheichelbauer (@mekkablue).
Based on sample code by Georg Seifert (@schriftgestalt) and Jan Gerner (@yanone).

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

See the License file included in this repository for further details.


