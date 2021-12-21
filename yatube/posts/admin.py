from django.contrib import admin

from .models import Post
from .models import Group


class PostAdmin(admin.ModelAdmin):
    # Display these fields in admin panel
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group'
    )
    # Edit groups from Posts
    list_editable = ('group',)
    # Interface for search
    search_fields = ('text',)
    # Filter by publish date
    list_filter = ('pub_date',)
    # If empty display this string
    empty_value_display = '-пусто-'


# Reg config from PostAdmin
admin.site.register(Post, PostAdmin)
# Add group to admin panel
admin.site.register(Group)
