grt=["red","blue","white"]
grt[1]="green"#修改列表值
print(grt[-3:])
p_grt=grt.pop()#pop(列表索引)默认为最后一个
print(f"{grt}\n{p_grt}")
