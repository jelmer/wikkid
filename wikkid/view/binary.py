#
# Copyright (C) 2010 Wikkid Developers
#
# This file is part of Wikkid.
#
# Wikkid is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Wikkid.  If not, see <http://www.gnu.org/licenses/>

"""Views associated with binary files."""

from wikkid.interface.resource import IBinaryFile
from wikkid.view.base import BaseView


class BinaryFile(BaseView):
    """Renders a binary file with its mimetype."""

    for_interface = IBinaryFile
    name = 'view'
    is_default = True

    def _render(self, skin):
        self.request.setHeader('Content-Type', self.context.mimetype)
        return self.context.get_bytes()