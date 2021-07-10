### macros used for the website

def define_env(env):
    @env.macro
    def tool_icon(icon_name, branch_name='1.1.0'):
        '''
        This generates a URL to the specified icon in the Xournal++ repository.
        '''
        # TODO: the website build should download all the icons so that they're
        # available standalone.
        return (
          'https://raw.githubusercontent.com/xournalpp/xournalpp/{}'
          '/ui/iconsColor-dark/hicolor/scalable/actions/{}'
        ).format(branch_name, icon_name)
