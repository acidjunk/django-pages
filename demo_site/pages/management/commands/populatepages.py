"""
A management command to populate the pages with some test content
"""
import random

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.models import Q

from ...models import Page, PageArticle, PageFAQ, PageLink, PageFacebookLink, PageYoutubeLink, GridCell

class Command(BaseCommand):
    """
    This class provides methods for generating pages to populate the pages module with some test content
    """
    args = ''
    help = 'Will populate the pages extensions with some test pages.'

    def __init__(self):
        try:
            self.user = User.objects.filter(Q(is_superuser=True)).first()
        except ObjectDoesNotExist:
            self.user = None

        super(Command, self).__init__()

    def _get_order_number(self, parent_page=None):
        try:
            order_number = Page.objects.filter(parent=parent_page).latest('ordering').ordering + 1
        except:
            order_number = 0
        return order_number

    def _create_random_grid_row(self, page, vertical_position):
        # Todo: rewrite to use Brian Grid validator (from the model)
        cols = random.randint(1, 5)  # 1-4 cols
        done = False
        while not done:
            sizes = random.sample(range(1, 17), cols)
            if sum(sizes) <= 16:
                done = True

        # for i in range(1, cols):
        #     pos = 0
        #     cell = GridCell()
        #     cell.page = page
        #     cell.horizontalPosition = pos
        #     cell.horizontalSize = sizes.pop()
        #     pos += cell.horizontalSize
        #     cell.verticalPosition = vertical_position
        #     cell.verticalSize = 1
        #     cell.save()
        #     i += 1

    def create_page(self, slug, name, slogan='', summary='', parent_page=None, sidebar_right=True):
        """
        This method generates a single page
        :return:
        """
        page = Page()
        page.slug = slug
        page.name = name
        page.slogan = slogan
        page.summary = summary
        page.parent = parent_page
        page.ordering = self._get_order_number()
        page.sidebar_right = True
        page.created_by = self.user
        page.modified_by = self.user
        page.save()

        # generate some fake/random grid content
        rows = random.randint(1, 10)  # 1-4 cols
        for i in range(1, rows):
            self._create_random_grid_row(page, i)
            i += 1
        return page


    def handle(self, *args, **options):
        """
        This method is invoked with the 'python manage populate_accounts' command.
        :param args: Command line arguments
        :param options: Command line options
        """
        Page.objects.all().delete()
        self.create_page('home', 'Home')
        page = self.create_page('about-us', 'About us', summary='A lot of info about our fictional organisation')
        self.create_page('history', 'History', parent_page=page)
        self.create_page('vision', 'Vision', parent_page=page)
        self.create_page('services', 'Serices', parent_page=page)
        page = self.create_page('test', 'Test', slogan='Test page with all possible content')
        sub_page1 = self.create_page('sub-1', 'Sub page 1', parent_page=page)
        self.create_page('sub-2', 'Sub page 2', parent_page=page)
        sub_page2 = self.create_page('sub-1-1', 'Sub sub page 1', parent_page=sub_page1)
        self.create_page('sub-1-2', 'Sub sub page 2', parent_page=sub_page1)
        self.create_page('sub-1-1-1', 'Sub sub sub page 1', parent_page=sub_page2)
        self.create_page('sub-1-1-2', 'Sub sub sub page 2', parent_page=sub_page2)
        self.create_page('contact', 'Contact')


