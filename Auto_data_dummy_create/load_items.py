"""
Copy file to: dsfm_general/management/commands/load_items.py
How to run: python manage.py load_items
Ref document: https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/
"""
import random
from datetime import date
from datetime import timedelta


from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from dsfm_general.models import Project, StoreType, ImageCategory, ImageType,\
    QCReasonCategory, QCReason, Employee, Sku, Planogram, Region, Store, UserInProject

from django.contrib.auth.models import User


class Command(BaseCommand):
    """
    This command
    """

    def handle(self, *args, **options):
        self.create_image_categories()
        self.create_qc_reason_categories()
        self.create_qc_reasons()

        self.create_projects()
        self.create_store_types()
        self.create_image_types()
        self.create_employee()
        self.create_store()
        self.create_user_in_project()
        self.create_admin_super_user()

    def create_admin_super_user(self):
        User.objects.all().delete()
        list_user = ['admin', 'admin1', 'root']
        counter = 0
        try:
            for i in list_user:
                counter += 1
                User.objects.create_superuser(
                    username=i,
                    password=f'{i}@123',
                    email=f'{i}@gmail.com'
                )
        except IntegrityError as error:
            print(error)
        else:
            self.stdout.write("Create %s SupperUserAdmin done " % counter)

    def create_image_categories(self):
        ImageCategory.objects.all().delete()

        num_of_items = 3
        counter = 0
        list_item = []

        for i in range(num_of_items):
            counter = counter + 1

            idx_code = str(counter).zfill(3)
            list_item.append(
                ImageCategory(
                    code=f"IMG_CATEG_TEST_{idx_code}",
                    name=f"ImageCategory Test {idx_code}",
                )
            )

        try:
            ImageCategory.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s ImageCategory done" % counter)
            self.stdout.write("Create %s ImageCategory done" % counter)

    def create_qc_reason_categories(self):
        QCReasonCategory.objects.all().delete()

        num_of_items = 3
        counter = 0
        list_item = []

        for i in range(num_of_items):
            counter = counter + 1

            idx_code = str(counter).zfill(3)
            list_item.append(
                QCReasonCategory(
                    code=f"QCREASON_CATEG_TEST_{idx_code}",
                    label=f"QC Reason Category Test {idx_code}",
                )
            )

        try:
            QCReasonCategory.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s QCReasonCategory done" % counter)
            self.stdout.write("Create %s QCReasonCategory done" % counter)

    def create_qc_reasons(self):
        QCReason.objects.all().delete()
        qc_reason_categories = QCReasonCategory.objects.all()

        num_of_items = 3
        counter = 0
        list_item = []

        for qc_reason_category in qc_reason_categories:
            for i in range(num_of_items):
                counter = counter + 1

                idx_code = str(counter).zfill(3)
                list_item.append(
                    QCReason(
                        code=f"QCReason_TEST_{idx_code}",
                        label=f"QC Reason Test {idx_code}",
                        qc_reason_category=qc_reason_category,
                    )
                )

        try:
            QCReason.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s QCReason done" % counter)
            self.stdout.write("Create %s QCReason done" % counter)

    def create_projects(self):
        Project.objects.all().delete()

        num_of_items = 3
        counter = 0
        list_item = []
        current_date = date.today()

        for i in range(num_of_items):
            counter = counter + 1
            random_number_of_days = random.randrange(10)
            start_date = current_date - timedelta(days=random_number_of_days)
            end_date = start_date + timedelta(days=20)
            active_date = start_date + timedelta(days=25)

            idx_code = str(counter).zfill(3)
            list_item.append(
                Project(
                    code=f"PROJECT_TEST_{idx_code}",
                    name=f"Project Test {idx_code}",
                    start_date=start_date,
                    end_date=end_date,
                    active_date=active_date,
                )
            )

        try:
            Project.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s projects done" % counter)
            self.stdout.write("Create %s projects done" % counter)

    def create_store_types(self):
        StoreType.objects.all().delete()
        projects = Project.objects.all()

        num_of_items = 3
        counter = 0
        list_item = []

        for project in projects:
            for i in range(num_of_items):
                counter = counter + 1

                idx_code = str(counter).zfill(3)
                list_item.append(
                    StoreType(
                        code=f"STORETYPE_TEST_{idx_code}",
                        name=f"StoreType Test {idx_code}",
                        project=project,
                    )
                )
        try:
            StoreType.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s StoreType done" % counter)
            self.stdout.write("Create %s StoreType done" % counter)

    def create_image_types(self):
        ImageType.objects.all().delete()
        projects = Project.objects.all()
        image_categories = ImageCategory.objects.all()

        num_of_items = 3
        counter = 0
        list_item = []

        for project in projects:
            for image_category in image_categories:
                for i in range(num_of_items):
                    counter = counter + 1

                    idx_code = str(counter).zfill(3)
                    list_item.append(
                        ImageType(
                            code=f"ImageType_TEST_{idx_code}",
                            name=f"ImageType Test {idx_code}",
                            project=project,
                            image_category=image_category,
                        )
                    )

        try:
            ImageType.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s ImageType done" % counter)
            self.stdout.write("Create %s ImageType done" % counter)

    def create_employee(self):
        Employee.objects.all().delete()

        num_of_items = 3
        counter = 0
        list_item = []

        for i in range(num_of_items):
            counter = counter + 1
            # start_date = current_date - timedelta(days=random_number_of_days)
            # end_date = start_date + timedelta(days=20)
            # active_date = start_date + timedelta(days=25)

            idx_code = str(counter).zfill(3)
            list_item.append(
                Employee(
                    username=f"FIELD_TEST_{idx_code}",
                    full_name=f"Field Test {idx_code}",
                    role='FIELD',
                    birth_date='2020-10-19',
                    password=f'field{idx_code}',
                    salt='123',
                )
            )

        list_users = ['admin', 'admin1', 'root']
        for i in list_users:
            counter += 1
            list_item.append(
                Employee(
                    username=i,
                    password=f'{i}@123',
                    role='ADMIN',
                    birth_date='1990-10-19',
                    salt='123',

                )
            )

        try:
            Employee.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s projects done" % counter)
            self.stdout.write("Create %s employee done" % counter)

    def create_store(self):
        Store.objects.all().delete()
        project = Project.objects.all().first()
        store_type = StoreType.objects.all().first()
        num_of_items = 3
        counter = 0
        list_item = []

        for i in range(num_of_items):
            counter = counter + 1
            idx_code = str(counter).zfill(3)
            list_item.append(
                Store(
                    code=f"STORE_TEST_{idx_code}",
                    project=project,
                    store_type=store_type,
                    lat='10.762622',
                    lng='106.660172',
                    specified_radius='50',
                )
            )

        try:
            Store.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s projects done" % counter)
            self.stdout.write("Create %s Store done" % counter)

    def create_user_in_project(self):
        UserInProject.objects.all().delete()
        project = Project.objects.all().first()
        fields = Employee.objects.filter(role='FIELD')
        list_item = []
        counter = 0
        for field in fields:
            counter += 1
            list_item.append(
                UserInProject(
                    field=field,
                    project=project
                )
            )
        try:
            UserInProject.objects.bulk_create(list_item)
        except IntegrityError as error:
            print(error)
        else:
            # print(f"* Create %s projects done" % counter)
            self.stdout.write(
                f"Create %s UserInProject for project {project} done" % counter)
