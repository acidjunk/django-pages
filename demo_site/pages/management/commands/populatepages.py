"""
A management command to populate the pages with some test content
"""
import random

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from ...models import Page, PageArticle, PageFAQ, PageLink, PageFacebookLink, PageYoutubeLink, GridCell

class Command(BaseCommand):
    """
    This class provides methods for generating pages to populate the pages module with some test content
    """
    args = ''
    help = 'Will populate the pages extensions with some test pages.'
    articles = []
    faqs = []
    youtubes = []
    content_types = ['pagearticle', 'pagefaq', 'pageyoutubelink']

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

    def _create_article(self, slug, name, content):
        article = PageArticle()
        article.slug = slug
        article.name = name
        article.content = content
        article.save()
        return article

    def _create_faq(self, slug, question, answer):
        faq = PageFAQ()
        faq.slug = slug
        faq.question = question
        faq.answer = answer
        faq.save()
        return faq

    def _create_youtube(self, slug, name, link):
        youtube = PageYoutubeLink()
        youtube.slug = slug
        youtube.name = name
        youtube.link = link
        youtube.save()
        return youtube

    def _create_random_grid_row(self, page, vertical_position):
        cols = random.randint(1, 5)  # 1-4 cols
        done = False
        while not done:
            sizes = random.sample(range(1, 17), cols)
            if sum(sizes) <= 16:
                done = True

        for i in range(1, cols):
            pos = 0
            cell = GridCell()
            cell.page = page
            cell.horizontalPosition = pos
            cell.horizontalSize = sizes.pop()
            pos += cell.horizontalSize
            cell.verticalPosition = vertical_position
            cell.verticalSize = 1

            model=random.choice(self.content_types)
            selected_content_type = ContentType.objects.get(model=model)
            cell.content_type = selected_content_type
            if model=='pagearticle': cell.object_pk = random.choice(self.articles).pk
            elif model=='pagefaq': cell.object_pk = random.choice(self.faqs).pk
            elif model=='pageyoutubelink': cell.object_pk = random.choice(self.youtubes).pk
            else:
                pass

            cell.save()
            i += 1

    def create_content(self):
        """Create some content that can be used on pages"""
        PageArticle.objects.all().delete()
        self.articles.append(self._create_article('art1', 'Test article 1',
                                            '<h2>Fancy subtitle</h2><p>This is a short test article. You can find the src code on <a href="https://github.com/acidjunk/django-pages">Github</a>.'))
        self.articles.append(self._create_article('art2', 'Test article 2',
            """<h2 class="ui center aligned icon header">
                <i class="circular users icon"></i>
                    Friends
            </h2>
            <div class="ui piled segment">
              <h4 class="ui header">A header</h4>
              <p>Te eum doming eirmod, nominati pertinacia argumentum ad his. Ex eam alia facete scriptorem, est autem aliquip detraxit at. Usu ocurreret referrentur at, cu epicurei appellantur vix. Cum ea laoreet recteque electram, eos choro alterum definiebas in. Vim dolorum definiebas an. Mei ex natum rebum iisque.</p>
               <p>Audiam quaerendum eu sea, pro omittam definiebas ex. Te est latine definitiones. Quot wisi nulla ex duo. Vis sint solet expetenda ne, his te phaedrum referrentur consectetuer. Id vix fabulas oporteat, ei quo vide phaedrum, vim vivendum maiestatis in.</p>
               <p>Eu quo homero blandit intellegebat. Incorrupte consequuntur mei id. Mei ut facer dolores adolescens, no illum aperiri quo, usu odio brute at. Qui te porro electram, ea dico facete utroque quo. Populo quodsi te eam, wisi everti eos ex, eum elitr altera utamur at. Quodsi convenire mnesarchum eu per, quas minimum postulant per id.</p>
            </div>
            """))
        self.articles.append(self._create_article('art3', 'Test article 3',
            """<div class="ui cards">
                  <div class="card">
                    <div class="content">
                      <img class="right floated mini ui image" src="/images/avatar/large/elliot.jpg">
                      <div class="header">
                        Elliot Fu
                      </div>
                      <div class="meta">
                        Friends of Veronika
                      </div>
                      <div class="description">
                        Elliot requested permission to view your contact details
                      </div>
                    </div>
                    <div class="extra content">
                      <div class="ui two buttons">
                        <div class="ui basic green button">Approve</div>
                        <div class="ui basic red button">Decline</div>
                      </div>
                    </div>
                  </div>
                  <div class="card">
                    <div class="content">
                      <img class="right floated mini ui image" src="/images/avatar/large/jenny.jpg">
                      <div class="header">
                        Jenny Hess
                      </div>
                      <div class="meta">
                        New Member
                      </div>
                      <div class="description">
                        Jenny wants to add you to the group <b>best friends</b>
                      </div>
                    </div>
                    <div class="extra content">
                      <div class="ui two buttons">
                        <div class="ui basic green button">Approve</div>
                        <div class="ui basic red button">Decline</div>
                      </div>
                    </div>
                  </div>
                </div>"""))

        PageFAQ.objects.all().delete()
        self.faqs.append(self._create_faq('faq1', 'What is the answer to live, the universe and everything?', '42'))
        self.faqs.append(self._create_faq('faq2', 'How does this work?', 'It works just fine'))
        self.faqs.append(self._create_faq('faq3', 'Where do I find the source code of this project?',
                                    'You can find the src code on <a href="https://github.com/acidjunk/django-pages">Github</a>.'))

        PageYoutubeLink.objects.all().delete()
        self.youtubes.append(self._create_youtube('you1', 'Youtube 1', 'https://www.youtube.com/watch?v=WhBoR_tgXCI'))
        self.youtubes.append(self._create_youtube('you2', 'Youtube 2', 'https://www.youtube.com/watch?v=VIpNrRCI48E'))
        self.youtubes.append(self._create_youtube('you3', 'Youtube 3', 'https://www.youtube.com/watch?v=dD69XD45epU'))
        self.youtubes.append(self._create_youtube('you4', 'Youtube 4', 'https://www.youtube.com/watch?v=6feEE716UEk'))
        self.youtubes.append(self._create_youtube('you5', 'Youtube 5', 'https://www.youtube.com/watch?v=1maD5WzsEs8'))
        self.youtubes.append(self._create_youtube('you6', 'Youtube 6', 'https://www.youtube.com/watch?v=eOVMD6fjDCo'))

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
            # content types:
            self._create_random_grid_row(page, i)
            i += 1
        return page



    def handle(self, *args, **options):
        """
        This method is invoked with the 'python manage populate_accounts' command.
        :param args: Command line arguments
        :param options: Command line options
        """
        # Genarte some test content
        self.create_content()

        # Prepare page DB
        Page.objects.all().delete()
        # Start filling
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


