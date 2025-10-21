# 🎯 Exercícios Práticos - NEO Project

## 📚 Exercícios para Aprofundamento em POO

### 🏗️ **Nível Iniciante - Fundamentos de POO**

#### **Exercício 1: Adicionar Métodos à Classe NearEarthObject**
```python
# Adicione os seguintes métodos à classe NearEarthObject:

class NearEarthObject:
    # ... código existente ...
    
    def get_approaches_count(self):
        """Retorna o número de aproximações conhecidas."""
        # TODO: Implementar
        pass
    
    def get_closest_approach(self):
        """Retorna a aproximação mais próxima da Terra."""
        # TODO: Implementar
        pass
    
    def get_fastest_approach(self):
        """Retorna a aproximação com maior velocidade."""
        # TODO: Implementar
        pass
    
    def is_larger_than(self, other_neo):
        """Compara se este NEO é maior que outro."""
        # TODO: Implementar
        pass
```

#### **Exercício 2: Implementar Métodos de Serialização**
```python
# Adicione métodos de serialização mais específicos:

class NearEarthObject:
    def to_dict(self):
        """Converte para dicionário Python."""
        # TODO: Implementar
        pass
    
    def to_json(self):
        """Converte para string JSON."""
        # TODO: Implementar
        pass
    
    @classmethod
    def from_dict(cls, data):
        """Cria instância a partir de dicionário."""
        # TODO: Implementar
        pass
```

### 🎨 **Nível Intermediário - Design Patterns**

#### **Exercício 3: Implementar Observer Pattern**
```python
# Crie um sistema de notificações para aproximações próximas:

class ApproachObserver:
    """Interface para observadores de aproximações."""
    def notify(self, approach):
        raise NotImplementedError

class EmailNotifier(ApproachObserver):
    """Notifica por email."""
    def notify(self, approach):
        # TODO: Implementar notificação por email
        pass

class LogNotifier(ApproachObserver):
    """Registra no log."""
    def notify(self, approach):
        # TODO: Implementar logging
        pass

class NEODatabase:
    def __init__(self, neos, approaches):
        # ... código existente ...
        self._observers = []  # Lista de observadores
    
    def add_observer(self, observer):
        """Adiciona um observador."""
        # TODO: Implementar
        pass
    
    def notify_observers(self, approach):
        """Notifica todos os observadores."""
        # TODO: Implementar
        pass
```

#### **Exercício 4: Implementar Builder Pattern**
```python
# Crie um builder para consultas complexas:

class QueryBuilder:
    def __init__(self):
        self._criteria = {}
    
    def with_date(self, date):
        """Adiciona filtro de data."""
        # TODO: Implementar
        return self
    
    def with_distance_range(self, min_dist, max_dist):
        """Adiciona filtro de distância."""
        # TODO: Implementar
        return self
    
    def with_hazardous_only(self):
        """Filtra apenas NEOs perigosos."""
        # TODO: Implementar
        return self
    
    def build(self):
        """Constrói a consulta final."""
        # TODO: Implementar
        pass

# Uso:
query = (QueryBuilder()
         .with_date(date(2020, 1, 1))
         .with_distance_range(0.1, 0.5)
         .with_hazardous_only()
         .build())
```

### 🚀 **Nível Avançado - Arquitetura e Performance**

#### **Exercício 5: Implementar Cache com Decorator Pattern**
```python
# Crie um sistema de cache para consultas:

import functools
import time
from typing import Dict, Any

class QueryCache:
    def __init__(self, max_size=1000, ttl=300):
        self._cache: Dict[str, Any] = {}
        self._timestamps: Dict[str, float] = {}
        self.max_size = max_size
        self.ttl = ttl  # Time to live em segundos
    
    def get(self, key):
        """Recupera valor do cache."""
        # TODO: Implementar com verificação de TTL
        pass
    
    def set(self, key, value):
        """Armazena valor no cache."""
        # TODO: Implementar com limite de tamanho
        pass
    
    def clear(self):
        """Limpa o cache."""
        # TODO: Implementar
        pass

def cached_query(cache_instance):
    """Decorator para cache de consultas."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Implementar cache
            pass
        return wrapper
    return decorator

# Uso:
cache = QueryCache(max_size=500, ttl=600)

class NEODatabase:
    @cached_query(cache)
    def query(self, filters=()):
        # ... implementação existente ...
        pass
```

#### **Exercício 6: Implementar Repository Pattern**
```python
# Crie uma camada de abstração para acesso a dados:

from abc import ABC, abstractmethod
from typing import List, Optional

class NEORepository(ABC):
    """Interface para repositório de NEOs."""
    
    @abstractmethod
    def find_by_designation(self, designation: str) -> Optional[NearEarthObject]:
        pass
    
    @abstractmethod
    def find_by_name(self, name: str) -> Optional[NearEarthObject]:
        pass
    
    @abstractmethod
    def find_all(self) -> List[NearEarthObject]:
        pass
    
    @abstractmethod
    def find_hazardous(self) -> List[NearEarthObject]:
        pass

class CSVNEORepository(NEORepository):
    """Implementação usando arquivo CSV."""
    
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self._neos = self._load_neos()
    
    def _load_neos(self):
        # TODO: Implementar carregamento do CSV
        pass
    
    def find_by_designation(self, designation: str):
        # TODO: Implementar busca por designação
        pass
    
    # ... outros métodos ...

class DatabaseNEORepository(NEORepository):
    """Implementação usando banco de dados."""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
    
    def find_by_designation(self, designation: str):
        # TODO: Implementar busca no banco
        pass
    
    # ... outros métodos ...
```

### 🧪 **Exercícios de Testes**

#### **Exercício 7: Testes Unitários Avançados**
```python
# Crie testes mais abrangentes:

import unittest
from unittest.mock import Mock, patch
from datetime import date

class TestNEODatabaseAdvanced(unittest.TestCase):
    
    def setUp(self):
        """Setup para cada teste."""
        # TODO: Implementar setup
        pass
    
    def test_query_performance(self):
        """Testa performance de consultas."""
        # TODO: Implementar teste de performance
        pass
    
    def test_concurrent_access(self):
        """Testa acesso concorrente."""
        # TODO: Implementar teste de concorrência
        pass
    
    def test_memory_usage(self):
        """Testa uso de memória."""
        # TODO: Implementar teste de memória
        pass
    
    @patch('database.NEODatabase._load_data')
    def test_database_initialization_with_mock(self, mock_load):
        """Testa inicialização com mock."""
        # TODO: Implementar teste com mock
        pass
```

#### **Exercício 8: Testes de Integração**
```python
# Crie testes de integração:

class TestIntegration(unittest.TestCase):
    
    def test_end_to_end_query_workflow(self):
        """Testa fluxo completo de consulta."""
        # TODO: Implementar teste end-to-end
        pass
    
    def test_data_consistency(self):
        """Testa consistência dos dados."""
        # TODO: Implementar teste de consistência
        pass
    
    def test_error_handling(self):
        """Testa tratamento de erros."""
        # TODO: Implementar teste de erros
        pass
```

### 📊 **Exercícios de Análise de Dados**

#### **Exercício 9: Implementar Análise Estatística**
```python
# Crie funcionalidades de análise:

class NEOAnalyzer:
    def __init__(self, database: NEODatabase):
        self.database = database
    
    def get_statistics(self):
        """Retorna estatísticas gerais."""
        # TODO: Implementar estatísticas
        pass
    
    def find_most_dangerous_neos(self, limit=10):
        """Encontra NEOs mais perigosos."""
        # TODO: Implementar análise de perigo
        pass
    
    def analyze_approach_patterns(self):
        """Analisa padrões de aproximação."""
        # TODO: Implementar análise de padrões
        pass
    
    def predict_future_approaches(self, days_ahead=365):
        """Prediz aproximações futuras."""
        # TODO: Implementar predição
        pass
```

#### **Exercício 10: Implementar Visualizações**
```python
# Crie visualizações dos dados:

import matplotlib.pyplot as plt
import pandas as pd

class NEOVisualizer:
    def __init__(self, database: NEODatabase):
        self.database = database
    
    def plot_distance_distribution(self):
        """Plota distribuição de distâncias."""
        # TODO: Implementar gráfico de distribuição
        pass
    
    def plot_velocity_over_time(self):
        """Plota velocidade ao longo do tempo."""
        # TODO: Implementar gráfico temporal
        pass
    
    def create_hazard_heatmap(self):
        """Cria mapa de calor de perigosidade."""
        # TODO: Implementar mapa de calor
        pass
    
    def generate_report(self, output_path: str):
        """Gera relatório completo."""
        # TODO: Implementar geração de relatório
        pass
```

### 🔧 **Exercícios de Refatoração**

#### **Exercício 11: Implementar Configuração Externa**
```python
# Crie sistema de configuração:

# config.yaml
"""
database:
  csv_path: "data/neos.csv"
  json_path: "data/cad.json"
  
query:
  default_limit: 10
  max_results: 1000
  
cache:
  enabled: true
  max_size: 500
  ttl: 300
  
logging:
  level: INFO
  file: "neo_project.log"
"""

import yaml
from dataclasses import dataclass
from typing import Optional

@dataclass
class DatabaseConfig:
    csv_path: str
    json_path: str

@dataclass
class QueryConfig:
    default_limit: int
    max_results: int

@dataclass
class CacheConfig:
    enabled: bool
    max_size: int
    ttl: int

@dataclass
class LoggingConfig:
    level: str
    file: str

class Config:
    def __init__(self, config_path: str = "config.yaml"):
        # TODO: Implementar carregamento de configuração
        pass
    
    def load_config(self):
        # TODO: Implementar carregamento
        pass
```

#### **Exercício 12: Implementar Logging Avançado**
```python
# Crie sistema de logging:

import logging
import logging.handlers
from datetime import datetime

class NEOLogger:
    def __init__(self, name: str, log_file: str = "neo_project.log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # File handler
        file_handler = logging.handlers.RotatingFileHandler(
            log_file, maxBytes=1024*1024, backupCount=5
        )
        
        # Console handler
        console_handler = logging.StreamHandler()
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def log_query(self, filters, result_count):
        """Log de consultas."""
        # TODO: Implementar logging de consultas
        pass
    
    def log_performance(self, operation, duration):
        """Log de performance."""
        # TODO: Implementar logging de performance
        pass
    
    def log_error(self, error, context=None):
        """Log de erros."""
        # TODO: Implementar logging de erros
        pass
```

### 🎯 **Soluções dos Exercícios**

Para cada exercício, considere:

1. **Implementação**: Código funcional e testado
2. **Testes**: Testes unitários para cada funcionalidade
3. **Documentação**: Docstrings e comentários explicativos
4. **Performance**: Considerações de eficiência
5. **Error Handling**: Tratamento robusto de erros

### 📚 **Recursos Adicionais**

- **Design Patterns**: Gang of Four
- **Python OOP**: `@property`, `@classmethod`, `@staticmethod`
- **Testing**: `pytest`, `unittest.mock`
- **Performance**: `cProfile`, `memory_profiler`
- **Visualization**: `matplotlib`, `plotly`, `seaborn`

---

*Exercícios desenvolvidos para aprofundar o conhecimento em Programação Orientada a Objetos e Design Patterns em Python.*
