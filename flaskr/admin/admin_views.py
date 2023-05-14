from flask import redirect, url_for
from flask_admin import AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import upload
from flask_ckeditor import CKEditorField
from flask_login import current_user
from config import Config
from flask_admin.contrib.fileadmin import FileAdmin

from flaskr.utils import constants


class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('users.login'))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        # 验证用户身份是不是超级用户
        if current_user.is_super == constants.UserRole.SUPER_ADMIN.value:
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('users.login'))


class MyView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('users.logout'))


class MyFileAdmin(FileAdmin):
    column_labels = dict(name='文件/目录', size='文件大小', date='添加时间')


class InfoAdmin(MyModelView):
    column_list = ('user_id', 'name', 'mobile', 'birthday', 'registration_items', 'match', 'match_id')
    column_labels = dict(name='姓名', mobile='手机号', birthday='生日',
                         registration_items='报名项目', add_time='报名时间', match_id='比赛序号', match='比赛',
                         user='用户', user_id='用户ID')
    page_size = 50
    can_set_page_size = True
    can_export = True
    export_types = ['xls', 'xlsx']
    column_sortable_list = ['birthday', 'add_time', 'match_id']
    column_searchable_list = ['mobile', 'name']
    column_filters = ['birthday', 'match_id', 'match_id', 'name']
    column_default_sort = 'add_time'
    column_export_exclude_list = ['match_id']
    can_view_details = True
    column_details_list = (
        'user_id', 'name', 'mobile', 'birthday', 'registration_items', 'add_time', 'match', 'match_id')
    column_export_list = ['user_id', 'name', 'mobile', 'birthday', 'registration_items', 'add_time', 'match',
                          'match_id']


class CompetitionInformationAdmin(MyModelView):
    form_overrides = dict(details=CKEditorField)  # 重写表单字段，将 detail 字段设为 CKEditorField
    create_template = 'edit.html'  # 指定创建记录的模板
    edit_template = 'edit.html'  # 指定编辑记录的模板
    column_labels = dict(id='比赛序号', match_time='比赛日期', address='地址', number_of_applicants='人数限制',
                         project_opening='开设项目', match_name='比赛名称', registration_fee='基础报名费',
                         registration_end_time='报名截止', details='详情', enter_status='录入状态', user='发布者',
                         item_registration_free='项目报名费', name='发布者姓名')
    page_size = 50
    can_set_page_size = True
    can_export = True
    column_sortable_list = ['match_time', 'registration_end_time', 'id', 'registration_fee', 'number_of_applicants']
    column_default_sort = ('match_time', 'desc')
    export_types = ['xls', 'xlsx']
    column_searchable_list = ['match_name', 'match_time', 'id']
    column_list = ('id', 'match_name', 'address', 'match_time', 'user')
    column_filters = ['match_name', 'match_time', 'project_opening', 'id', 'user.name']
    column_export_exclude_list = ['detail']
    can_view_details = True
    form_columns = ('user', 'match_name', 'address', 'number_of_applicants', 'project_opening', 'match_time',
                    'registration_fee', 'item_registration_free', 'registration_end_time', 'details')


class BannerAdmin(MyModelView):
    page_size = 50
    can_set_page_size = True
    can_export = True
    column_labels = dict(image_route='图片路径', add_time='添加时间', index='索引')
    column_descriptions = dict(image_route='上传格式：gif，jpg，jpeg，png')
    form_extra_fields = {'image_route': upload.ImageUploadField(
        label=u'轮播图', base_path=Config.UPLOADED_PATH, relative_path='banner/',
        allow_overwrite=['gif', 'jpg', 'jpeg', 'png'], )}


class UserAdmin(MyModelView):
    column_labels = dict(username='用户名', password='密码', name='名称', status='状态', is_super='权限',
                         created_at='创建时间', sex='性别', birthday='生日', )
    page_size = 50
    can_set_page_size = True
    can_export = True
    column_sortable_list = ['username', 'name', 'is_super', 'birthday', 'created_at', 'status', 'sex']
    export_types = ['xls', 'xlsx']
    column_searchable_list = ['username', 'name', 'created_at']
    column_list = ('username', 'name', 'sex', 'birthday', 'created_at', 'status', 'is_super')
    column_filters = ['username', 'name', 'is_super', 'birthday', 'sex', 'created_at']
    can_view_details = True
    column_details_list = ('username', 'name', 'sex', 'birthday', 'created_at', 'status', 'is_super')
    form_columns = ('username', 'name', 'sex', 'birthday', 'created_at', 'status', 'is_super')


class OderInfoAdmin(MyModelView):
    page_size = 50
    can_set_page_size = True
    can_export = True
    column_labels = dict(oder_id='订单号', add_time='添加时间', amount='金额', user='用户')


class UserLoginHistoryAdmin(MyModelView):
    page_size = 100
    can_set_page_size = True
    can_export = True
    column_list = ('user', 'username', 'ip', 'created_at')
    column_labels = dict(ip='IP地址', ua='请求头', user='用户', created_at='登录时间', username='用户名')
    can_view_details = True
    column_details_list = ('user', 'ip', 'username', 'created_at', 'ua')


class UserProfileAdmin(MyModelView):
    page_size = 50
    can_set_page_size = True
    can_export = True
    column_labels = dict(profile='用户', avatar='头像文件名')


class IndexArticleAdmin(MyModelView):
    page_size = 50
    can_set_page_size = True
    can_export = True
    form_overrides = dict(content=CKEditorField)  # 重写表单字段，将 detail 字段设为 CKEditorField
    create_template = 'edit.html'  # 指定创建记录的模板
    edit_template = 'edit.html'  # 指定编辑记录的模板
    column_labels = dict(user='用户', title='标题', release_time='发布时间', content='内容')
    column_list = ('user', 'title', 'release_time')
    can_view_details = True
    column_details_list = ('user', 'title', 'release_time', 'content')


class AchievementCuberAdmin(MyModelView):
    page_size = 50
    can_set_page_size = True
    can_export = True
    column_labels = dict(competition_options='类型', user='用户', match='比赛', birthday='生日', match_id='比赛号',
                         user_id='用户ID',
                         competition_information='比赛', match_name='名称', sex='性别', name='名字', match_time='时间')
    column_sortable_list = ['t1', 't2', 't3', 't4', 't5', 'best', 'ao5']
    column_default_sort = ('best', 'ao5')
    export_types = ['xls', 'xlsx']
    column_searchable_list = ['match_id', 'user_id']
    column_list = ('user', 'match', 't1', 't2', 't3', 't4', 't5',
                   'best', 'ao5', 'competition_options')
    column_filters = ['match.match_name', 'match.id', 'match.match_time', 'user.sex',
                      'user.birthday', 'user.name', 'user.id', 'competition_options']
    can_view_details = True
    column_details_list = ('user', 'match', 't1', 't2', 't3', 't4', 't5',
                           'best', 'ao5', 'competition_options')


class AchievementCuber333Admin(AchievementCuberAdmin):
    pass


class AchievementCuber222Admin(AchievementCuberAdmin):
    pass


class AchievementCuberOhAdmin(AchievementCuberAdmin):
    pass


class AchievementCuberSkAdmin(AchievementCuberAdmin):
    pass


class AchievementCuberPyAdmin(AchievementCuberAdmin):
    pass
