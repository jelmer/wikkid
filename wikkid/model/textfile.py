#
# Copyright (C) 2010 Wikkid Developers.
#
# This software is licensed under the GNU Affero General Public License
# version 3 (see the file LICENSE).

"""The source text class.

A source text file is a text file that isn't a wiki file.
"""

from zope.interface import implements

from wikkid.model.file import FileResource
from wikkid.interface.resource import ITextFile


class TextFile(FileResource):
    """A text file that isn't a wiki page."""

    implements(ITextFile)

    def __repr__(self):
        return "<TextFile '%s'>" % self.path
