+def Tampil_Tuple(tuple):
+	for i in range(len(tuple)): # for i in range(len(tuplee)):  == tuplee diganti dengan tuple == 	
+		print(i+1,'.',tuple[i])   # print(i+1,'.',tuplee[i])  == tuplee diganti dengan tuple ==   
+
+def Tampil_List(list):
+	for i in list:              # for i in listing:  == listing diganti dengan list ==   
+		print(i)
+
+def Utama():
+	list=[1,2,3,4,5,6,7,8,9]
+	tuple=('Aria Hendrawan','Basworo Ardi Pramono','Khoirudin','April Firman Daru','Whisnumurti')
+	print("\nBerikut adalah angka keberuntungan saya ")
+	Tampil_List(list)
+	print("\n-----------------------------------------")
+	print("Daftar Nama Dosen FTIK USM ")
+	Tampil_Tuple(tuple)
+
+Utama();                       # Utama(args)  == args dihapus ==   
+
+
+# == HASIL RUNNING ==
+# Berikut adalah angka keberuntungan saya 
+# 1
+# 2
+# 3
+# 4
+# 5
+# 6
+# 7
+# 8
+# 9
+# 
+# -----------------------------------------
+# Daftar Nama Dosen FTIK USM 
+# (1, '.', 'Aria Hendrawan')
+# (2, '.', 'Basworo Ardi Pramono')
+# (3, '.', 'Khoirudin')
+# (4, '.', 'April Firman Daru')
+# (5, '.', 'Whisnumurti')
