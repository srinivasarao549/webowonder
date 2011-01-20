# -*- coding: utf-8 -*-
"""Example views. Feel free to delete this app."""

import itertools

import jingo

from tower import ugettext as _

from demos.models import Submission

# TODO, need actual urls and such
tags = {
    # L10n: Tag MDN urls. You can change these if your locale has a better url
    'Audio':       (_('https://developer.mozilla.org/en/Introducing_the_Audio_API_Extension'), 
    # L10n: Technology Tags. A demo can have up to 5 of these. Keep them short.
                    _('Audio')),
    'Canvas':      (_('https://developer.mozilla.org/En/Canvas'), 
                    _('Canvas')),
    'CSS3':        (_('https://developer.mozilla.org/En/CSS'),
                    _('CSS3')),
    'DnD':         (_('https://developer.mozilla.org/en/DragDrop/Drag_and_Drop'),
                    _('DnD')),
    'Files':       (_('https://developer.mozilla.org/en/using_files_from_web_applications'),
                    _('Files')), 
    'Fonts':       (_('https://developer.mozilla.org/en/css/@font-face'),
                    _('Fonts')),
    'Forms':       (_('https://developer.mozilla.org/en/HTML/HTML5/Forms_in_HTML5'),
                    _('Forms')),
    'GeoLocation': (_('https://developer.mozilla.org/En/Using_geolocation'), 
                    _('GeoLocation')),
    'JavaScript':  (_('https://developer.mozilla.org/En/javascript'), 
                    _('JavaScript')), 
    'HTML5':       (_('https://developer.mozilla.org/En/HTML5/HTML5'),
                    _('HTML5')), 
    'Mobile':      (_('https://developer.mozilla.org/En/Mobile'),
                    _('Mobile')), 
    'MultiTouch':  (_('https://developer.mozilla.org/En/MultiTouch'),
                    _('MultiTouch')),
    'SVG':         (_('https://developer.mozilla.org/En/SVG'), 
                    _('SVG')), 
    'Video':       (_('https://developer.mozilla.org/En/Using_audio_and_video_in_Firefox'),
                    _('Video')), 
    'WebGL':       (_('https://developer.mozilla.org/En/WebGL'),
                    _('WebGL')), 
     # L10n: Last of the Technology Tags.
    'XMLHttpRequest': (_('https://developer.mozilla.org/En/XMLHttpRequest/Using_XMLHttpRequest'),
                    _('XMLHttpRequest')),
}

def home(request):
    global tags
    data = {'demos': Submission.objects.filter(hidden=False)}
    for demo in data['demos']:

        ltags = [(tags[x.strip()][0], tags[x.strip()][1],) for x in demo.tags.split(',')]
        tag_pairs = list(itertools.chain(*ltags))

        # This may be ugly to a programmer, but the simplicity
        # is for ease of L10n. Please don't make this more terse
        copy = None
        if len(ltags) == 1:
            # L10n {1} is a tag like HTML5 or GeoLocation {0} is a url
            copy = _("Built with <a href='{0}'>{1}</a>.")
        elif len(ltags) == 2:
            # L10n {1} and {3} are tags like HTML5 and GeoLocation, {0} and {2} are urls
            copy = _("Built with <a href='{0}'>{1}</a> and <a href='{2}'>{3}</a>.")
        elif len(ltags) == 3:
            copy = _("Built with <a href='{0}'>{1}</a>, <a href='{2}'>{3}</a> and <a href='{4}'>{5}</a>.")
        elif len(ltags) == 4:
            copy = _("Built with <a href='{0}'>{1}</a>, <a href='{2}'>{3}</a>, <a href='{4}'>{5}</a> and <a href='{6}'>{7}</a>.")
        elif len(ltags) == 5:
            copy = _("Built with <a href='{0}'>{1}</a>, <a href='{2}'>{3}</a>, <a href='{4}'>{5}</a>, <a href='{6}'>{7}</a> and <a href='{8}'>{9}</a>.")

        if copy:
            demo.tag_copy = copy.format(*tag_pairs)

        # L10n {0} is the title of a demo
        demo.video_title = _('The Making of {0}').format(demo.title)
        # TODO new db field
        demo.video_description = 'See how John Smith brothers brought space down to earth.'

    return jingo.render(request, 'wow/home.html', data)
