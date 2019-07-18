from django.db import models

class Intelligence_result_log(models.Model):
    intelligence_id =models.CharField(max_length=255)
    event_id = models.CharField(max_length=255)
    links = models.CharField(max_length=1024)
    type = models.IntegerField(max_length=3)
    operate_time = models.IntegerField(max_length=10)
    operate_uid = models.IntegerField(max_length=20)
    create_time = models.IntegerField(max_length=10)
    update_time = models.IntegerField(max_length=10)
    is_deleted = models.IntegerField(max_length=3)
    open_links =models.CharField(max_length=1296)
    operate_type=models.IntegerField(max_length=3)
    road_name = models.CharField(max_length=255)
    reason =models.CharField(max_length=255)
    detail =models.CharField(max_length=255)
    remind =models.CharField(max_length=255)
    COMMENT =models.CharField(max_length=255)
    event_geo =models.CharField(max_length=255)
    start_time =models.IntegerField(max_length=10)
    end_time =models.IntegerField(max_length=10)
    weekdays =models.CharField(max_length=255)
    pace_ride_limit=models.CharField(max_length=255)
    start_hour=models.IntegerField(max_length=10)
    end_hour =models.IntegerField(max_length=10)
    event_type=models.IntegerField(max_length=10)


    class Meta:
        db_table = "intelligence_result_log"  # 更改表名
