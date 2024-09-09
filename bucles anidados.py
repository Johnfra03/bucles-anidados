# Matriz 3D: ciudades (3), semanas (4), días de la semana (7 días)
nuevas_temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 65},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 75}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 64},
            {"day": "Martes", "temp": 66},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 71},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 78}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 66},
            {"day": "Martes", "temp": 68},
            {"day": "Miércoles", "temp": 71},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 75},
            {"day": "Sábado", "temp": 79},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 68},
            {"day": "Martes", "temp": 70},
            {"day": "Miércoles", "temp": 72},
            {"day": "Jueves", "temp": 74},
            {"day": "Viernes", "temp": 76},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 79}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 55},
            {"day": "Martes", "temp": 57},
            {"day": "Miércoles", "temp": 60},
            {"day": "Jueves", "temp": 62},
            {"day": "Viernes", "temp": 65},
            {"day": "Sábado", "temp": 68},
            {"day": "Domingo", "temp": 70}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 56},
            {"day": "Martes", "temp": 58},
            {"day": "Miércoles", "temp": 61},
            {"day": "Jueves", "temp": 64},
            {"day": "Viernes", "temp": 67},
            {"day": "Sábado", "temp": 69},
            {"day": "Domingo", "temp": 72}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 54},
            {"day": "Martes", "temp": 56},
            {"day": "Miércoles", "temp": 59},
            {"day": "Jueves", "temp": 63},
            {"day": "Viernes", "temp": 66},
            {"day": "Sábado", "temp": 68},
            {"day": "Domingo", "temp": 71}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 57},
            {"day": "Martes", "temp": 59},
            {"day": "Miércoles", "temp": 62},
            {"day": "Jueves", "temp": 65},
            {"day": "Viernes", "temp": 68},
            {"day": "Sábado", "temp": 70},
            {"day": "Domingo", "temp": 73}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 85},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 91},
            {"day": "Viernes", "temp": 90},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 87}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 86},
            {"day": "Martes", "temp": 88},
            {"day": "Miércoles", "temp": 90},
            {"day": "Jueves", "temp": 92},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 85}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 87},
            {"day": "Martes", "temp": 89},
            {"day": "Miércoles", "temp": 91},
            {"day": "Jueves", "temp": 93},
            {"day": "Viernes", "temp": 88},
            {"day": "Sábado", "temp": 86},
            {"day": "Domingo", "temp": 84}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 88},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 92},
            {"day": "Jueves", "temp": 94},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 85}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad por semana
for i, ciudad in enumerate(nuevas_temperaturas):
    print(f"\nPromedio de temperaturas para Ciudad {i+1}:")
    for j, semana in enumerate(ciudad):
        suma = 0
        for dia in semana:
            suma += dia['temp']
        promedio = suma / len(semana)
        print(f"  Semana {j+1}: {promedio:.2f}°F")
