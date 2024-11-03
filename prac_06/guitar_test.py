from guitar import Guitar

# 创建 Guitar 对象
guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(guitar)  # 打印对象，检查 __str__ 方法

# 测试 get_age 方法
print(f"Age of the guitar: {guitar.get_age()} years")  # 输出年龄

# 测试 is_vintage 方法
print(f"Is the guitar vintage? {'Yes' if guitar.is_vintage() else 'No'}")  # 检查是否复古
