import matplotlib.pyplot as plt
import numpy as np

# 重新排序的参数组合和对应的准确率 - 按窗口大小组织，形成"山峰"形状
combinations = ['Window 0.6\nStep 50%', 
                'Window 0.6\nStep 1', 
                'Window 1.0\nStep 1', 
                'Window 1.3\nStep 50%',
                'Window 1.3\nStep 1']

# 对应重新排序的准确率值
mean_accuracies = [0.6292945073047008,  # Window 0.6, Step 50%
                   0.6571569060934012,  # Window 0.6, Step 1
                   0.9524760890792976,  # Window 1.0, Step 1 (peak)
                   0.8453583185522333,  # Window 1.3, Step 50%
                   0.8802960612463361]  # Window 1.3, Step 1

# 创建图表 - 更紧凑的尺寸
plt.figure(figsize=(8, 6))

# 创建条形图，使用一致的颜色方案：深色表示Step 1（精确搜索），浅色表示Step 50%（粗略搜索）
colors = ['#FFB74D',  # Window 0.6, Step 50% - 浅橙色
          '#FF8F00',  # Window 0.6, Step 1 - 深橙色
          '#2E7D32',  # Window 1.0, Step 1 - 深绿色（最优结果）
          '#81C784',  # Window 1.3, Step 50% - 浅绿色
          '#388E3C']  # Window 1.3, Step 1 - 深绿色

bars = plt.bar(combinations, mean_accuracies, color=colors, edgecolor='black', linewidth=1.2, alpha=0.8, width=0.5)

# 设置Y轴
plt.ylabel('Mean Accuracy (F1 Score)', fontsize=12, fontweight='bold')
plt.ylim(0, 1.0)

# 添加更详细的网格线，便于数值对比
plt.grid(axis='y', alpha=0.6, linestyle='-', linewidth=0.5, color='gray')
# 添加特定位置的网格线
y_grid_positions = [0.2, 0.4, 0.6, 0.8]
for y_pos in y_grid_positions:
    plt.axhline(y=y_pos, color='lightgray', linestyle='--', alpha=0.7, linewidth=1)

# 设置X轴，调整标签角度避免重叠
plt.xlabel('Parameter Combinations', fontsize=12, fontweight='bold')
plt.xticks(rotation=30, ha='right', fontsize=10)

# 设置标题 - 减小padding让图表更紧凑
plt.title('Medieval Irish to Modern Irish: Algorithm Performance Evaluation', 
          fontsize=13, fontweight='bold', pad=15)

# 在每个条形上添加精确数值
for bar, accuracy in zip(bars, mean_accuracies):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.01,
             f'{accuracy:.4f}', ha='center', va='bottom', fontsize=9, fontweight='bold')



# 优化布局 - 使用更紧凑的设置
plt.tight_layout(pad=1.5)

# 保存图表到当前目录
plt.savefig('evaluation_results.png', dpi=300, bbox_inches='tight')

# 显示图表（注释掉以避免弹出窗口）
# plt.show()
print("图表已保存为 'evaluation_results.png'")

# 打印统计信息
print("=" * 50)
print("Evaluation Results Summary")
print("=" * 50)
for i, (combo, acc) in enumerate(zip(combinations, mean_accuracies), 1):
    combo_name = combo.replace('\n', ', ')
    print(f"Combination {i} ({combo_name}): {acc:.4f}")

print(f"\nBest performing combination: {combinations[np.argmax(mean_accuracies)].replace(chr(10), ', ')}")
print(f"Best accuracy: {max(mean_accuracies):.4f}")
print(f"Average accuracy across all combinations: {np.mean(mean_accuracies):.4f}")
print(f"Standard deviation: {np.std(mean_accuracies):.4f}")

# 生成一个更详细的分析表格（可选）
import pandas as pd

# 创建详细数据表（按新的排序）
detailed_data = {
    'Combination': [f'C{i+1}' for i in range(5)],
    'Window Size': [0.6, 0.6, 1.0, 1.3, 1.3],
    'Step Size': ['50%', '1', '1', '50%', '1'],
    'Mean Accuracy': mean_accuracies,
    'Performance': ['High' if acc > 0.7 else 'Medium' for acc in mean_accuracies]
}

df = pd.DataFrame(detailed_data)
print("\n" + "=" * 50)
print("Detailed Results Table")
print("=" * 50)
print(df.to_string(index=False))

# 保存表格到CSV
df.to_csv('evaluation_results_table.csv', index=False)
print("\nResults saved to:")
print("- evaluation_results.png (graph)")
print("- evaluation_results.pdf (graph)")
print("- evaluation_results_table.csv (data table)")