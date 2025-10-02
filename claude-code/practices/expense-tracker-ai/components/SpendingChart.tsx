'use client';

import React from 'react';
import { Expense, Category } from '@/types/expense';
import { getCategoryColor } from '@/lib/utils';

interface SpendingChartProps {
  expenses: Expense[];
}

export default function SpendingChart({ expenses }: SpendingChartProps) {
  const categoryTotals: Record<Category, number> = {
    Food: 0,
    Transportation: 0,
    Entertainment: 0,
    Shopping: 0,
    Bills: 0,
    Other: 0,
  };

  expenses.forEach(expense => {
    categoryTotals[expense.category] += expense.amount;
  });

  const total = Object.values(categoryTotals).reduce((sum, amount) => sum + amount, 0);

  const chartData = Object.entries(categoryTotals)
    .map(([category, amount]) => ({
      category: category as Category,
      amount,
      percentage: total > 0 ? (amount / total) * 100 : 0,
    }))
    .filter(item => item.amount > 0)
    .sort((a, b) => b.amount - a.amount);

  const maxAmount = Math.max(...chartData.map(item => item.amount), 1);

  if (chartData.length === 0) {
    return (
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Spending Overview</h3>
        <div className="text-center py-8">
          <p className="text-gray-500">No data to display</p>
        </div>
      </div>
    );
  }

  return (
    <div className="bg-white rounded-lg shadow p-6">
      <h3 className="text-lg font-semibold text-gray-900 mb-6">Spending Overview</h3>

      {/* Bar Chart */}
      <div className="space-y-4 mb-8">
        {chartData.map(({ category, amount, percentage }) => (
          <div key={category} className="space-y-2">
            <div className="flex items-center justify-between text-sm">
              <span className="font-medium text-gray-700">{category}</span>
              <span className="text-gray-900 font-semibold">
                ${amount.toFixed(2)}
              </span>
            </div>
            <div className="relative w-full h-8 bg-gray-100 rounded-lg overflow-hidden">
              <div
                className={`${getCategoryColor(category)} h-full transition-all duration-500 flex items-center justify-end pr-3`}
                style={{ width: `${(amount / maxAmount) * 100}%` }}
              >
                <span className="text-white text-xs font-medium">
                  {percentage.toFixed(1)}%
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Pie Chart Representation */}
      <div className="border-t pt-6">
        <h4 className="text-sm font-semibold text-gray-700 mb-4">Distribution</h4>
        <div className="flex flex-wrap gap-3">
          {chartData.map(({ category, percentage }) => (
            <div key={category} className="flex items-center gap-2">
              <div className={`w-3 h-3 rounded-full ${getCategoryColor(category)}`} />
              <span className="text-sm text-gray-600">
                {category} ({percentage.toFixed(1)}%)
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
