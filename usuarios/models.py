from django.db import models

# 2º opção (já tem o usuário base com as funcionalidades prontas para ser utilizada)
from django.contrib.auth.models import AbstractUser, BaseUserManager

#Esse gerenciador de usuário para o usuário da classe abaixo. Esse gerenciador é responsável por salvar tanto usuário comum quanto de admin
class UsuarioManager(BaseUserManager):

    use_in_migrations = True #informando que irá virar uma tabela após o comando makemigrations

    # O metodo abaixo será usado pelo metodo create_user e superuser
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        # Define o username como o email (ou outro valor único)
        username = extra_fields.get('username', email)  # Usa o email como username, se não for fornecido
        extra_fields.setdefault('username', username) #novas linhas acrescentada

        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)#criptografa a senha.
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        #extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        
        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    fone =models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email
    
    objects = UsuarioManager()