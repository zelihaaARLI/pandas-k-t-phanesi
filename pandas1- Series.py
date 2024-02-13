import pandas as pd #pip install pandas
import numpy as np #pip install numpy
#öncelikle serilere bakıp ondan sonra  dataframelere başlayabiliriz;
#We can look at the series first, then start with the dataframe.
#Series komutu =>indekslerle beraber alt alta yazdirir;
# prints indexes and values together one under the other
#example
seri=pd.Series([9,8,7,9,6,5])
print(seri)

seri1=pd.Series([1,2,3,4,5,6,6])
print(seri1)

#seri.indeks =>indeks bilgileri verir; 
#gives index information
seri=pd.Series([1,2,3,4,5,6])
print(seri.index)

#seri.size =>serideki eleman sayisini verir; 
#Returns the number of elements in the series
seri=pd.Series([1,2,3,4,5,6,7,8])
print(seri.size)

#seri.ndim=> serinin boyutu bilgisini  verir; 
#gives the size information of the series
seri=pd.Series([1,2,3,4,5,2,3,4])
print(seri.ndim)

#seri.values=>değerlere array formunda erişmek icin kulanilir;
# It allows us to access the values in the series in array form
seri=pd.Series([1,2,3,4,5,6,7])
print(seri.values)

#seri.head()=>fonksiyonun icine giren değer kadar veriyi gösterir;
# Prints data up to the value entered in the function
seri=pd.Series([1,2,3,4,1,2,34,3])
print(seri.head(3))

#seri.tail() =>fonksiyonun sondAN İSTENİLEN KADAR DEĞERDE ELEMAN VERİR;
# Returns data from the end as much as the value entered into the function
seri=pd.Series([1,2,3,4,56,4,56])
print(seri.tail(3))

#indeks  adlari değiştirme!(indekse istediğimiz adi verebiliriz str int float vb. farketmez);
# change index names
seri=pd.Series([1,2,3,4,56,8],index=["a","b","c","d","e","f"])
print(seri)

#sözlükleri seriye cevirme;
# converting dictionaries to serialization
#example
sozluk={"ay":45,"can":54,"su":20,"ali":67}
seriSozluk=pd.Series(sozluk)
print(seriSozluk)

sozluk1={"buğra":19,"kerem":89,"elif":26,"murat":76,"pelin":67}
serisozluk1=pd.Series(sozluk1)
print(serisozluk1)

#indeksleme ve slicing process(işlemi)
#examples
seriler=pd.Series([1,2,3,4,56,7])
print(seriler[1])
print(seriler[4])
print(seriler[1:])
print(seriler[::-1])
print(seriler[3:5])

#random sayilarla işlemler ;random numbers process
#example
dizi=np.random.randint(50,size=6)
seriledizi=pd.Series(dizi,index=["a","b","c","d","e","f"])
print(seriledizi)
print(seriledizi[["b","d"]])
print(seriledizi[["a","f"]])
seriledizi[["b","f"]]=55
print(seriledizi)