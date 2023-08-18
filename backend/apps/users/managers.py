from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_kwargs):
        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password if password else self.make_random_password())
        user.save()
        return user

    def get_or_create_students_or_get_mentor(self, email):
        email = self.normalize_email(email)
        user, created = self.get_or_create(email=email)

        if created:
            user.set_password(self.make_random_password())
            user.save()

        return user, created

    def create_superuser(self, email, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_manager', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)
        extra_kwargs.setdefault('password', '')

        if extra_kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, **extra_kwargs)

    def create_manager(self, email, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_manager', True)
        extra_kwargs.setdefault('is_active', False)
        extra_kwargs.setdefault('password', '')

        if extra_kwargs.get('is_staff') is not True:
            raise ValueError('Manager must have is_staff=True')
        if extra_kwargs.get('is_manager') is not True:
            raise ValueError('Manager must have is_manager=True')
        return self.create_user(email, **extra_kwargs)

    def create_mentor(self, email, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_active', False)
        extra_kwargs.setdefault('password', '')

        if extra_kwargs.get('is_staff') is not True:
            raise ValueError('Mentor must have is_staff=True')
        return self.create_user(email, **extra_kwargs)

    def get(self, *args, **kwargs):
        return super().select_related('profile').get(*args, **kwargs)

    def all(self):
        return super().select_related('profile').all()

    def managers(self):
        return self.filter(is_manager=True, is_superuser=False)

    def mentors(self):
        return self.filter(is_staff=True, is_superuser=False, is_manager=False)
