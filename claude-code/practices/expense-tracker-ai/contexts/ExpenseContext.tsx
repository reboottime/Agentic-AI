'use client';

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { Expense, ExpenseFormData, Category } from '@/types/expense';
import { localStorageUtil } from '@/lib/localStorage';
import { generateId } from '@/lib/utils';

interface ExpenseContextType {
  expenses: Expense[];
  addExpense: (formData: ExpenseFormData) => void;
  updateExpense: (id: string, formData: ExpenseFormData) => void;
  deleteExpense: (id: string) => void;
  loading: boolean;
}

const ExpenseContext = createContext<ExpenseContextType | undefined>(undefined);

export const ExpenseProvider = ({ children }: { children: ReactNode }) => {
  const [expenses, setExpenses] = useState<Expense[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadedExpenses = localStorageUtil.getExpenses();
    setExpenses(loadedExpenses);
    setLoading(false);
  }, []);

  const addExpense = (formData: ExpenseFormData) => {
    const now = new Date().toISOString();
    const newExpense: Expense = {
      id: generateId(),
      date: formData.date,
      amount: parseFloat(formData.amount),
      category: formData.category,
      description: formData.description,
      createdAt: now,
      updatedAt: now,
    };

    const updatedExpenses = [...expenses, newExpense];
    setExpenses(updatedExpenses);
    localStorageUtil.saveExpenses(updatedExpenses);
  };

  const updateExpense = (id: string, formData: ExpenseFormData) => {
    const updatedExpenses = expenses.map(expense => {
      if (expense.id === id) {
        return {
          ...expense,
          date: formData.date,
          amount: parseFloat(formData.amount),
          category: formData.category,
          description: formData.description,
          updatedAt: new Date().toISOString(),
        };
      }
      return expense;
    });

    setExpenses(updatedExpenses);
    localStorageUtil.saveExpenses(updatedExpenses);
  };

  const deleteExpense = (id: string) => {
    const updatedExpenses = expenses.filter(expense => expense.id !== id);
    setExpenses(updatedExpenses);
    localStorageUtil.saveExpenses(updatedExpenses);
  };

  return (
    <ExpenseContext.Provider
      value={{
        expenses,
        addExpense,
        updateExpense,
        deleteExpense,
        loading,
      }}
    >
      {children}
    </ExpenseContext.Provider>
  );
};

export const useExpenses = () => {
  const context = useContext(ExpenseContext);
  if (context === undefined) {
    throw new Error('useExpenses must be used within an ExpenseProvider');
  }
  return context;
};
