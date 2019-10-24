from django.db import models

# Create your models here.
from django.shortcuts import render


class BaseTable(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        verbose_name_plural = verbose_name


# class UserInfo(BaseTable):
#     class Meta:
#         verbose_name = '用户信息'
#         db_table = 'UserInfo'
#
#     username = models.CharField('用户名', max_length=20, unique=True, null=False)
#     password = models.CharField('密码', max_length=20, null=False)
#     email = models.EmailField('邮箱', null=False, unique=True)
#     status = models.IntegerField('有效/无效', default=1)


class Project(BaseTable):
    """
    项目表
    """

    class Meta:
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name

    name = models.CharField("名称", max_length=50, null=False)
    describe = models.TextField("描述", default="")
    status = models.IntegerField("状态：", default=0)  # 0未执行、1执行完成

    def __str__(self):
        return self.name


class Module(BaseTable):
    """
     模块表
     """

    class Meta:
        verbose_name = '模块信息'
        verbose_name_plural = verbose_name

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=50, null=False)
    describe = models.TextField("描述", default="")

    # status = models.IntegerField("状态：", default=0)  # 0未执行、1执行中、2执行完成、3排队中

    def __str__(self):
        return self.name


class TestCase(BaseTable):
    """
    测试用例表
    """

    class Meta:
        verbose_name = '用例信息'
        verbose_name_plural = verbose_name

    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    name = models.CharField("名称", max_length=50, null=False)
    # status = models.BooleanField("状态", default=True)   # 控制用例的删除
    url = models.TextField("URL", null=False)
    # 1:GET, 2: POST, 3:DELETE, 4:PUT
    method = models.IntegerField("请求方法", null=False)
    header = models.TextField("请求头", null=False)
    parameter_type = models.IntegerField("参数类型", null=False)  # 1：form-data 2: json
    parameter_body = models.TextField("参数内容", null=False)
    result = models.TextField("结果", null=False)
    assert_type = models.IntegerField("断言类型", null=False)  # 1：包含contains 2: 匹配mathches
    assert_text = models.TextField("结果", null=False)
    # environment_id = models.IntegerField("环境id", null=False)

    def __str__(self):
        return self.name


class Environment(BaseTable):
    """
    环境表
    """

    class Meta:
        verbose_name = '环境'
        verbose_name_plural = verbose_name

    # environment = models.ForeignKey(TestCase)
    name = models.CharField("名称", max_length=50, null=False)
    address = models.CharField("地址", max_length=50, null=False)
    status = models.IntegerField("状态：", default=0)  # 1开启 0停用

    def __str__(self):
        return self.name

# class TestTask(models.Model):
#     """
#     任务表
#     """
#
#     class Meta:
#         verbose_name = '任务'
#         verbose_name_plural = verbose_name
#
#     name = models.CharField("名称", max_length=100, blank=False, default="")
#     describe = models.TextField("描述", default="")
#     status = models.IntegerField("状态：", default=0)  # 0未执行、1执行中、2执行完成、3排队中
#     cases = models.TextField("关联用例", default="")
#     create_time = models.DateTimeField("创建时间", auto_now_add=True)
#
#     def __str__(self):
#         return self.name
