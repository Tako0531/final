from django.db import models

# Create your models here.
class LogItem(models.Model):
  # 處理進度的選項清單
  ST_OPTIONS = [
    (0, '未認證'),
    (1, '未通過'),
    (2, '舊社長認證'),
    (3, '新社長認證'),
    (4, '新老師認證'),
    (5, '舊老師認證'),
    (6, '組長認證'),
  ]
  # 報修主旨
  subject = models.CharField('申請人員', max_length=20)
  # 報修內容
  description = models.TextField('轉社原因')
  # 報修時間
  ctime = models.DateTimeField('報修時間', auto_now_add=True)
  # --------------------------------------------------
  # 處理人員
  handler = models.CharField('處理人員', max_length=30)
  # 處理進度
  status = models.IntegerField(
              '處理進度', 
              default=0, 
              choices=ST_OPTIONS
           )
  # 處理說明
  comment = models.TextField('處理說明')
  # 最後更新時間
  utime = models.DateTimeField('最後更新時間', auto_now=True)

  OLD_CHOICES = (
    (0, "未選擇"),
    (1, "1社"),
    (2, "2社"),
    (3, "3社"),
    (4, "4社"),
    (5, "5社"),
    (7, "6社"),
)
  old_club = models.IntegerField('舊社團', default=25, choices=OLD_CHOICES)
  new_club = models.IntegerField('新社團', default=25, choices=OLD_CHOICES)


  def __str__(self):
    return self.subject






  # 根據 status 的值傳回對應的 class 字串, 
  # 0 傳回 'danger', 1 傳回 'warning', 2 傳回 'success'
  #def get_status_class(self):
    #return ['danger', 'warning', 'success'][self.status]