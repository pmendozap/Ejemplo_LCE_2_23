# Laboratorio 0

* El comando `	ngspice -o out_l0_a.txt -b lab00_a.cir
` permite correr una simulación DC del circuito resistivo simple. El resultado queda almacenado en el archivo out_l0_a.txt.
* El comando `ngspice -b lab00_b.cir` permite correr la simulación usando una fuente senoidal a 1kHz del circuito resistivo simple. Los resultados quedan en el archivo out_00_b.txt

    * El comando `python3 lab00_a_dat.py` extrae de los resultaados de out_l0_a.txt y los grafica como se muestra a continuación:

![Curvas mostrando corriente y voltaje en la resistencia](docs/Figure_1.svg?raw=true "Corriente y voltaje en la resistencia")

![Curvas mostrando corriente y voltaje en la resistencia](docs/Figure_2.svg?raw=true "Corriente y voltaje en la resistencia")