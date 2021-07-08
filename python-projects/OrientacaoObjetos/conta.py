
from _typeshed import Self


class Conta:

  def __init__(self,numero=0,titular="",saldo=0.0,limite=0):
    self._numero  = numero
    self._titular = titular
    self._saldo   = saldo
    self._limite  = limite
  
  def extrato(self):
    print("Saldo de {} do titular {}".format(self._saldo,self._titular))
  
  def depositar(self,valor = 0):
    self._saldo += valor
  
  def sacar(self,valor = 0):
    self._saldo -= valor


      