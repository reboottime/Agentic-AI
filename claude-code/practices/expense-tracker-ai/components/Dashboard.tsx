'use client';

import React from 'react';
import { Expense, Category } from '@/types/expense';
import { formatCurrency, calculateSummary } from '@/lib/utils';

interface DashboardProps {
  expenses: Expense[];
}

export default function Dashboard({ expenses }: DashboardProps) {
  const summary = calculateSummary(expenses);

  const categoryData = Object.entries(summary.categoryBreakdown)
    .map(([category, amount]) => ({
      category: category as Category,
      amount,
      percentage:
        summary.totalSpending > 0 ? (amount / summary.totalSpending) * 100 : 0,
    }))
    .filter(item => item.amount > 0)
    .sort((a, b) => b.amount - a.amount);

  return (
    <div className="space-y-6">
      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {/* Total Spending */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between mb-2">
            <h3 className="text-sm font-medium text-gray-600">Total Spending</h3>
            <div className="p-2 bg-blue-100 rounded-lg">
              <svg
                className="w-5 h-5 text-blue-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </div>
          </div>
          <p className="text-3xl font-bold text-gray-900">
            {formatCurrency(summary.totalSpending)}
          </p>
          <p className="text-sm text-gray-500 mt-1">All time</p>
        </div>

        {/* Monthly Spending */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between mb-2">
            <h3 className="text-sm font-medium text-gray-600">This Month</h3>
            <div className="p-2 bg-green-100 rounded-lg">
              <svg
                className="w-5 h-5 text-green-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
                />
              </svg>
            </div>
          </div>
          <p className="text-3xl font-bold text-gray-900">
            {formatCurrency(summary.monthlySpending)}
          </p>
          <p className="text-sm text-gray-500 mt-1">
            {summary.totalSpending > 0
              ? `${((summary.monthlySpending / summary.totalSpending) * 100).toFixed(1)}% of total`
              : 'No spending yet'}
          </p>
        </div>

        {/* Total Expenses */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between mb-2">
            <h3 className="text-sm font-medium text-gray-600">Total Expenses</h3>
            <div className="p-2 bg-purple-100 rounded-lg">
              <svg
                className="w-5 h-5 text-purple-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                />
              </svg>
            </div>
          </div>
          <p className="text-3xl font-bold text-gray-900">{summary.expenseCount}</p>
          <p className="text-sm text-gray-500 mt-1">Transactions recorded</p>
        </div>

        {/* Top Category */}
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center justify-between mb-2">
            <h3 className="text-sm font-medium text-gray-600">Top Category</h3>
            <div className="p-2 bg-orange-100 rounded-lg">
              <svg
                className="w-5 h-5 text-orange-600"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z"
                />
              </svg>
            </div>
          </div>
          <p className="text-3xl font-bold text-gray-900">{summary.topCategory}</p>
          <p className="text-sm text-gray-500 mt-1">
            {formatCurrency(summary.categoryBreakdown[summary.topCategory])}
          </p>
        </div>
      </div>

      {/* Category Breakdown */}
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Spending by Category</h3>

        {categoryData.length === 0 ? (
          <div className="text-center py-8">
            <p className="text-gray-500">No expenses recorded yet</p>
          </div>
        ) : (
          <div className="space-y-4">
            {categoryData.map(({ category, amount, percentage }) => (
              <div key={category}>
                <div className="flex items-center justify-between mb-2">
                  <span className="text-sm font-medium text-gray-700">{category}</span>
                  <div className="flex items-center gap-3">
                    <span className="text-sm text-gray-500">
                      {percentage.toFixed(1)}%
                    </span>
                    <span className="text-sm font-semibold text-gray-900">
                      {formatCurrency(amount)}
                    </span>
                  </div>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div
                    className="bg-blue-600 h-2 rounded-full transition-all duration-500"
                    style={{ width: `${percentage}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
