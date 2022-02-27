# Iot_final_project

This is a final project of  ***Internet Of Things*** course(11010CS423500). We simulated the spraying process of framers and analyzed the uniformity of "pesticide" distribution, but I prefer to called it "Goodness of fit".

The network used in project is based on Narrowband Internet of things (NB-Iot) technology, which focuses on indoor coverage, low cost, long battery life and high connection density. Sensor/devices is **NB-4038**, it is a little box integrates GPS, G-sensor, Bluetooth, NB-Iot and battery. The instructions are pre-loaded and you could input commands through **nRF Toolbox** APP.

We use 2 methods to calculate the uniformity of distribution, Standard Deviation / Path Coverage(my teammate) and **[Kolmogorov–Smirnov](https://en.wikipedia.org/wiki/Kolmogorov–Smirnov_test)** test. You can see the codes in file : IoT_final_project_code_06_NB-IoT_program

Here are some tips :

1. Requested lib / package: numpy, scipy, pandas, matplotlib.pylot
2. Run **IoT_final_project_code_NB-IoT.py** or **IoT_final_project_code_NB-IoT噴藥均勻度分析.ipynb**
3. "aa.csv" in "素材" file is the GPS data. We download these from our course [website](https://nthu-smart-farming.kits.tw/), or you can try **MQTT.fx** to manually downlink data. First column in csv file is the date and the second column contains the GPS data
4. GPS data have specific format, the transformation from number to latitude and longitude can refer our PPT.
5. The visualization of GPS data are shown after running .py / .ipynb file
6. Output of KS-Test are **P-value** and **D-value**，meaning of these values also listed in the PPT.
7. My teammate recorded a [video](https://drive.google.com/file/d/1Hss5mVlHoSPjZ4FTDFf_TrtpRd1dDBlH/view?usp=sharing) to explain his code.

 PS：2D KS test reference:

​		https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html



If you have any questions, feel free to contact us : zhangsihao0413@gmail.com

