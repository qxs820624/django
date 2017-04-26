from django.db import models

##
# <p>A collection of the border-related attributes of an XF record.
# Items correspond to those in the Excel UI's Format/Cells/Border tab.</p>
# <p> An explanations of "colour index" is given in the Formatting
# section at the start of this document.
# There are five line style attributes; possible values and the
# associated meanings are:
# 0&nbsp;=&nbsp;No line,
# 1&nbsp;=&nbsp;Thin,
# 2&nbsp;=&nbsp;Medium,
# 3&nbsp;=&nbsp;Dashed,
# 4&nbsp;=&nbsp;Dotted,
# 5&nbsp;=&nbsp;Thick,
# 6&nbsp;=&nbsp;Double,
# 7&nbsp;=&nbsp;Hair,
# 8&nbsp;=&nbsp;Medium dashed,
# 9&nbsp;=&nbsp;Thin dash-dotted,
# 10&nbsp;=&nbsp;Medium dash-dotted,
# 11&nbsp;=&nbsp;Thin dash-dot-dotted,
# 12&nbsp;=&nbsp;Medium dash-dot-dotted,
# 13&nbsp;=&nbsp;Slanted medium dash-dotted.
# The line styles 8 to 13 appear in BIFF8 files (Excel 97 and later) only.
# For pictures of the line styles, refer to OOo docs s3.10 (p22)
# "Line Styles for Cell Borders (BIFF3-BIFF8)".</p>
# <br /> -- New in version 0.6.1
class XFBorder(models.Model):

    ##
    # The colour index for the cell's top line
    top_colour_index = models.IntegerField(default = 0)
    ##
    # The colour index for the cell's bottom line
    bottom_colour_index = models.IntegerField(default = 0)
    ##
    # The colour index for the cell's left line
    left_colour_index = models.IntegerField(default = 0)
    ##
    # The colour index for the cell's right line
    right_colour_index = models.IntegerField(default = 0)
    ##
    # The colour index for the cell's diagonal lines, if any
    diag_colour_index = models.IntegerField(default = 0)
    ##
    # The line style for the cell's top line
    top_line_style = models.IntegerField(default = 0)
    ##
    # The line style for the cell's bottom line
    bottom_line_style = models.IntegerField(default = 0)
    ##
    # The line style for the cell's left line
    left_line_style = models.IntegerField(default = 0)
    ##
    # The line style for the cell's right line
    right_line_style = models.IntegerField(default = 0)
    ##
    # The line style for the cell's diagonal lines, if any
    diag_line_style = models.IntegerField(default = 0)
    ##
    # 1 = draw a diagonal from top left to bottom right
    diag_down = models.IntegerField(default = 0)
    ##
    # 1 = draw a diagonal from bottom left to top right
    diag_up = models.IntegerField(default = 0)

##
# A collection of the background-related attributes of an XF record.
# Items correspond to those in the Excel UI's Format/Cells/Patterns tab.
# An explanation of "colour index" is given in the Formatting
# section at the start of this document.
# <br /> -- New in version 0.6.1
class XFBackground(models.Model):

    ##
    # See section 3.11 of the OOo docs.
    fill_pattern = models.IntegerField(default = 0)
    ##
    # See section 3.11 of the OOo docs.
    background_colour_index = models.IntegerField(default = 0)
    ##
    # See section 3.11 of the OOo docs.
    pattern_colour_index = models.IntegerField(default = 0)

##
# A collection of the alignment and similar attributes of an XF record.
# Items correspond to those in the Excel UI's Format/Cells/Alignment tab.
# <br /> -- New in version 0.6.1

class XFAlignment(models.Model):

    ##
    # Values: section 6.115 (p 214) of OOo docs
    hor_align = models.IntegerField(default = 0)
    ##
    # Values: section 6.115 (p 215) of OOo docs
    vert_align = models.IntegerField(default = 0)
    ##
    # Values: section 6.115 (p 215) of OOo docs.<br />
    # Note: file versions BIFF7 and earlier use the documented
    # "orientation" attribute; this will be mapped (without loss)
    # into "rotation".
    rotation = models.IntegerField(default = 0)
    ##
    # 1 = text is wrapped at right margin
    text_wrapped = models.IntegerField(default = 0)
    ##
    # A number in range(15).
    indent_level = models.IntegerField(default = 0)
    ##
    # 1 = shrink font size to fit text into cell.
    shrink_to_fit = models.IntegerField(default = 0)
    ##
    # 0 = according to context; 1 = left-to-right; 2 = right-to-left
    text_direction = models.IntegerField(default = 0)

##
# A collection of the protection-related attributes of an XF record.
# Items correspond to those in the Excel UI's Format/Cells/Protection tab.
# Note the OOo docs include the "cell or style" bit
# in this bundle of attributes.
# This is incorrect; the bit is used in determining which bundles to use.
# <br /> -- New in version 0.6.1

class XFProtection(models.Model):
    ##
    # 1 = Cell is prevented from being changed, moved, resized, or deleted
    # (only if the sheet is protected).
    cell_locked = models.IntegerField(default = 0)
    ##
    # 1 = Hide formula so that it doesn't appear in the formula bar when
    # the cell is selected (only if the sheet is protected).
    formula_hidden = models.IntegerField(default = 0)

##
# eXtended Formatting information for cells, rows, columns and styles.
# <br /> -- New in version 0.6.1
#
# <p>Each of the 6 flags below describes the validity of
# a specific group of attributes.
# <br />
# In cell XFs, flag==0 means the attributes of the parent style XF are used,
# (but only if the attributes are valid there); flag==1 means the attributes
# of this XF are used.<br />
# In style XFs, flag==0 means the attribute setting is valid; flag==1 means
# the attribute should be ignored.<br />
# Note that the API
# provides both "raw" XFs and "computed" XFs -- in the latter case, cell XFs
# have had the above inheritance mechanism applied.
# </p>

class XF(models.Model):
    
    # 0 = cell XF, 1 = style XF
    is_style = models.IntegerField(default = 0)
    # cell XF: Index into Book.xf_list
    # of this XF's style XF<br />
    # style XF: 0xFFF
    parent_style_index = models.IntegerField(default = 0)
    #
    _format_flag = models.IntegerField(default = 0)
    #
    _font_flag = models.IntegerField(default = 0)
    #
    _alignment_flag = models.IntegerField(default = 0)
    #
    _border_flag = models.IntegerField(default = 0)
    #
    _background_flag = models.IntegerField(default = 0)
    #  
    _protection_flag = models.IntegerField(default = 0)
    # Index into Book.xf_list
    xf_index = models.IntegerField(default = 0)
    # Index into Book.font_list
    font_index = models.IntegerField(default = 0)
    # Key into Book.format_map
    # <p>
    # Warning: OOo docs on the XF record call this "Index to FORMAT record".
    # It is not an index in the Python sense. It is a key to a map.
    # It is true <i>only</i> for Excel 4.0 and earlier files
    # that the key into format_map from an XF instance
    # is the same as the index into format_list, and <i>only</i>
    # if the index is less than 164.
    # </p>
    format_key = models.IntegerField(default = 0)
    # An instance of an XFProtection object.
    protection = models.ManyToManyField(XFProtection)
    # An instance of an XFBackground object.
    background = models.ManyToManyField(XFBackground)
    # An instance of an XFAlignment object.
    alignment = models.ManyToManyField(XFAlignment)
    # An instance of an XFBorder object.
    border = models.ManyToManyField(XFBorder)
    
    
class Format(models.Model):
    ##
    # The key into Book.format_map
    format_key = models.IntegerField(default= 0)
    ##
    # A classification that has been inferred from the format string.
    # Currently, this is used only to distinguish between numbers and dates.
    # <br />Values:
    # <br />FUN = 0 # unknown
    # <br />FDT = 1 # date
    # <br />FNU = 2 # number
    # <br />FGE = 3 # general
    # <br />FTX = 4 # text
    type =  models.IntegerField(default= 0) ## FUN
    ##
    # The format string
    format_str = models.CharField(max_length = 100) ## UNICODE_LITERAL('')

    def __unicode__(self):
        return self.format_str
    
########################################################################
class Colour(models.Model):
    """"""
    r =  models.IntegerField(name= "red", default= 0)
    g =  models.IntegerField(name= "green", default= 0)
    b =  models.IntegerField(name= "blue", default= 0)

    #----------------------------------------------------------------------
    def __unicode__(self):
        """Constructor"""
        return str(colourMap.index) + ":" + str((r, g, b))
        

########################################################################
class ColourMap(models.Model):
    """"""
    index = models.IntegerField(name= "index", default= 0)
    colour = models.ManyToManyField(Colour)
    #----------------------------------------------------------------------
    def __unicode__(self):
        """Constructor"""
        return str(index) + ":" + str(colour)


########################################################################
class WorkBook(models.Model):
    """"""
    userName = models.CharField(max_length = 30)
    codepage =  models.IntegerField(name= "codepage", null= True)
    countries = models.CharField(max_length = 10)
    encoding = models.CharField(max_length = 10, null = True)
    nsheets = models.IntegerField(default= 0)
    use_mmap = models.IntegerField(default= 0)
    formatting_info = models.IntegerField(default= 0)
    on_demand = models.IntegerField(default= 0)
    ragged_rows = models.IntegerField(default= 0)
    
    colourMap = models.ManyToManyField(ColourMap)
    xflist = models.ManyToManyField(XF)
    fmtlist = models.ManyToManyField(Format)
    
    #----------------------------------------------------------------------
    def __unicode__(self):
        """Constructor"""
        return self.userName
    
########################################################################
class Rowinfo(models.Model):
    height = models.IntegerField(default= 345)
    has_default_height = models.IntegerField(default= 0)
    outline_level = models.IntegerField(default= 0)
    outline_group_starts_ends = models.IntegerField(default= 0)
    hidden = models.IntegerField(default= 0)
    height_mismatch = models.IntegerField(default= 1)
    has_default_xf_index = models.IntegerField(default= 0)
    xf_index = models.IntegerField(default= -1)
    additional_space_above = models.IntegerField(default= 0)
    additional_space_below = models.IntegerField(default= 0)
    
class Colinfo(models.Model):
    ##
    # Width of the column in 1/256 of the width of the zero character,
    # using default font (first FONT record in the file).
    width = models.IntegerField(default= 12)
    ##
    # XF index to be used for formatting empty cells.
    xf_index = models.IntegerField(default= -1)
    ##
    # 1 = column is hidden
    hidden = models.IntegerField(default= 0)
    ##
    # Value of a 1-bit flag whose purpose is unknown
    # but is often seen set to 1
    bit1_flag = models.IntegerField(default= 1)
    ##
    # Outline level of the column, in range(7).
    # (0 = no outline)
    outline_level = models.IntegerField(default= 0)
    ##
    # 1 = column is collapsed
    collapsed = models.IntegerField(default= 0)
    
########################################################################
class Sheet(models.Model):
    """"""
    workBook =  models.ForeignKey(WorkBook)
    visibility = models.IntegerField(default= 0)
    sheetName = models.CharField(max_length=200)
    rowinfo_map = models.ManyToManyField(Rowinfo)
    nrows = models.IntegerField(default= 0)
    ncols = models.IntegerField(default= 0)
    
    #records = models.ForeignKey(Records,blank=True,null=True, on_delete=models.CASCADE)

    # on_delete 当一个model对象的ForeignKey关联的对象被删除时，默认情况下此对象也会一起被级联删除的。
    #DO_NOTHING:啥也不做。
    #CASCADE: 默认值，model对象会和ForeignKey关联对象一起被删除
    #SET_NULL:将model对象的ForeignKey字段设为null。当然需要将null设为True。
    #SET_DEFAULT:将model对象的ForeignKey字段设为默认值。
    #Protect:删除ForeignKey关联对象时会生成一个ProtectedError，这样ForeignKey关联对象就不会被删除了。
    #SET():将model对象的ForeignKey字段设为传递给SET()的值。
    #def get_sentinel_user():
        #return User.objects.get_or_create(username='deleted')[0]
    
    #class MyModel(models.Model):
        #user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
        

########################################################################
class crange(models.Model):
    """"""
    sheet = models.ForeignKey(Sheet)
    rlo = models.IntegerField(default= 0)
    rhi = models.IntegerField(default= 0)
    clo = models.IntegerField(default= 0)
    chi = models.IntegerField(default= 0)
    

########################################################################
class Merge(models.Model):
    """"""
    #col_label_ranges
    #row_label_ranges
    #merged_cells
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    rowStartIndex = models.IntegerField(default= 0)
    rowEndIndex = models.IntegerField(default= 0)
    colStartIndex = models.IntegerField(default= 0)
    colEndIndex = models.IntegerField(default= 0)

    def __unicode__(self):
        return str((self.rowStartIndex, self.rowEndIndex, self.colStartIndex, self.colEndIndex))
        

########################################################################
class Cell(models.Model):
    """"""
    sheet = models.ForeignKey(Rowinfo, on_delete=models.CASCADE)
    row = models.IntegerField(default=0)
    col = models.IntegerField(default=0)
    ctype = models.IntegerField(default=6) # 6 blank
    value = models.CharField(max_length=200)
    xf_index = models.IntegerField(null= True)
    # colour index
    bgx = models.IntegerField(default=64)
    
    #----------------------------------------------------------------------
    def __unicode__(self):
        return str(self.value)
