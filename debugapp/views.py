from django.shortcuts import render


from debug_toolbar.panels import Panel
from debug_toolbar.utils import ThreadCollector
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.views import View
from django.shortcuts import redirect
import psutil
from DebugToolbarEdit import settings

class SystemDetailsPanel(Panel):
    template = 'system_detail.html'
    nav_title = _("System Info")
    def title(self):
        return _("My Panel: System Info")
    def generate_stats(self, request, response):
        pids = psutil.pids()
        d = []
        for p in pids:
            pname = psutil.Process(p).name()
            pmem = psutil.Process(p).memory_info().rss
            d.append((p, pname, pmem))

        d.sort(key=lambda x: x[2])
        d = d[:50]

        processes = {}
        for proc in d:
            processes[proc[0]] = [proc[1], proc[2]]

        self.record_stats({'stats': processes})


class TicTacToe(Panel):
    #template="tictactoe.html"
    template="tictactoerender.html"
    nav_title=_("TicTacToe")
    title=_("Tic Tac Toe")


class TicTacToeView(View):
    def get(self,request):
        return render(request,"tictactoe.html",context={"ximg":"xnew.png","oimg":"o.png","blankimg":"blank.jpg",'media_url':settings.MEDIA_URL})

