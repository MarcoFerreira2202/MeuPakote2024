from django.db import models
from django.contrib.auth.models import User

# Create your models here.    

class Condominio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self) -> str:
        return self.nome
    
class Funcionario(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeF = models.CharField(max_length=100)
    condominio = models.ForeignKey('Condominio', on_delete=models.CASCADE, related_name='funcionarios')
    funcaoFuncionario = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nomeF
    
class Apartamento(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=10)
    #morador_principal = models.ForeignKey(Morador, on_delete=models.SET_NULL, null=True, blank=True, related_name='apartamentos')
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name='apartamentos')
    def __str__(self):
        return f"{self.numero} ({self.condominio})"
    
class Morador(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.CASCADE, related_name='apartamentos')
    email = models.EmailField()
    telefone = models.CharField(max_length=20)


    def __str__(self):
        return f'{self.nome} - {self.apartamento} - {self.apartamento.condominio}'
    
class Encomenda(models.Model):
    id = models.AutoField(primary_key=True)
    morador = models.ForeignKey(Morador, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    data_hora_recebimento = models.DateTimeField()
    data_hora_entrega = models.DateTimeField(blank=True, null=True)
    codigo_retirada = models.CharField(max_length=4, default='0000')
    funcionario_recebimento = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='funcionario_recebimento')
    funcionario_entrega = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='funcionario_entrega', blank=True, null=True)
    
    def __str__(self):
        return self.descricao
    
class Log(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.timestamp} - {self.user.username}: {self.message}"
