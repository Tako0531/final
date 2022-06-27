from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse
from .models import LogItem
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# 報修項目列表
class LogList(ListView):
      model = LogItem
      ordering = ['-id']
      paginate_by = 15

class LogView(DetailView):
  model = LogItem

# 新增報修項目
class LogCreate(CreateView):
  model = LogItem
  fields = ['subject', 'description', 'old_club', 'new_club']

  def get_success_url(self):
    return reverse('log_list')

  def get_success_url(self):
    return reverse('log_list')

# 回覆維修進度
class LogReply(LoginRequiredMixin, UpdateView):
  model = LogItem
  # 回覆時僅顯示相關欄位
  fields = ['handler', 'status', 'comment']
  template_name = 'log/logitem_detail.html'

  def get_success_url(self):
    return reverse('log_view', kwargs={'pk': self.object.id})

  def get_initial(self):
    data = {}
    # 取得目前登入的使用者資訊
    u = self.request.user
    # 如果有名字，就填名字，否則就填帳號名稱
    if u.first_name:
      data['handler'] = u.first_name
    else:
      data['handler'] = u.username
    return data

    #permissionrequiredmixin

    
