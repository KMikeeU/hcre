

class Mangler:
    def __init__(self):
        self.manglers = []

    def mangle(self, string):
        """
        Mangle a string with defined manglers
        """
        mangled = string

        for mangler in self.manglers:
            mangled = mangler(mangled)

        return mangled
        
    def add_mangler(self, mangler):
        """
        Add a mangler to the list of manglers
        """

        self.manglers.append(mangler)
    



    def mangle_lowercase(self):
        """
        Rule: l
         - Lowercase all letters
        """

        def _(string):
            return string.lower()
        
        return _

    def mangle_uppercase(self):
        """
        Rule: u
         - Uppercase all letters
        """

        def _(string):
            return string.upper()
        
        return _

    def mangle_capitalize(self):
        """
        Rule: c
         - Capitalize the first letter and lower the rest
        """

        def _(string):
            return string.lower().capitalize()

        return _
    
    def mangle_invert_capitalize(self):
        """
        Rule: C
         - Lowercase first found character, uppercase the rest
        """

        def _(string):
            return string[0].lower() + string[1:].upper()

        return _
    
    def mangle_toggle_case(self):
        """
        Rule: t
         - Toggle case of all letters
        """

        def _(string):
            return string.swapcase()
        
        return _
    
    def mangle_toggle_at(self, at):
        """
        Rule: TN
         - Toggle case of letter at position n
        """

        def _(string):
            return string[:at] + string[at].swapcase() + string[at+1:]
        
        return _
    
    def mangle_reverse(self):
        """
        Rule: r
         - Reverse the entire word
        """

        def _(string):
            return string[::-1]
        
        return _
    
    def mangle_duplicate(self):
        """
        Rule: d
         - Duplicate entire word
        """

        def _(string):
            return string + string
        
        return _
    
    def mangle_duplicate_n(self, n):
        """
        Rule: pN
         - Append duplicated word N time
        """

        def _(string):
            return string * n
        
        return _
    
    def mangle_reflect(self):
        """
        Rule: f
         - Duplicate word reversed
        """

        def _(string):
            return string + string[::-1]
        
        return _
    
    def mangle_rotate_left(self):
        """
        Rule: {
         - Rotate the word left.
        """

        def _(string):
            return string[1:] + string[0]
        
        return _
    
    def mangle_rotate_right(self):
        """
        Rule: }
         - Rotate the word right.
        """
            
        def _(string):
            return string[-1] + string[:-1]
        
        return _
    
    def mangle_append_character(self, X):
        """
        Rule: $X
         - Append character X to end
        """

        def _(string):
            return string + X
        
        return _
    
    def mangle_prepend_character(self, X):
        """
        Rule: ^X
         - Prepend character X to front
        """
        
        def _(string):
            return X + string
        
        return _
    
    def mangle_purge(self, X):
        """
        Rule: @X
         - Purge all instances of X
        """

        def _(string):
            return string.replace(X, "")
        
        return _
    
    def mangle_replace_character(self, X, Y):
        """
        Rule: sXY
         - Replace all instances of X with Y
        """

        def _(string):
            return string.replace(X, Y)
        
        return _