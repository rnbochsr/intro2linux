# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.712771
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/findpeersh.asm'
_template_uri = 'i386/linux/findpeersh.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nArgs: port (defaults to any)\n    Finds an open socket which connects to a specified\n    port, and then opens a dup2 shell on it.\n'
def render_body(context,port=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,port=port)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.shellcraft.i386 import linux 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['linux'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n\n')
        __M_writer(unicode(linux.findpeer(port)))
        __M_writer(u'\n\n')
        __M_writer(unicode(linux.dupsh("esi")))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 3, "33": 8, "34": 11, "35": 11, "36": 13, "37": 13, "43": 37, "16": 4, "17": 3, "22": 1, "26": 1, "27": 2, "31": 2}, "uri": "i386/linux/findpeersh.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/findpeersh.asm"}
__M_END_METADATA
"""
