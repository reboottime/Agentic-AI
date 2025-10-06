# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A modern, professional expense tracking web application built with Next.js 14, TypeScript, and Tailwind CSS. The application helps users manage their personal finances with an intuitive interface, complete expense management, filtering capabilities, and visual analytics.

## Technology Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Context API
- **Data Persistence**: localStorage (browser-based)
- **Font**: Inter (Google Fonts)

## Development Commands

```bash
# Install dependencies
npm install

# Run development server (with Turbopack)
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run linter
npm run lint
```

The development server runs at `http://localhost:3000`.

## Project Architecture

### Directory Structure

```
├── app/                    # Next.js app directory
│   ├── layout.tsx         # Root layout with ExpenseProvider
│   ├── page.tsx           # Main application page
│   └── globals.css        # Global styles
├── components/            # React components
│   ├── Dashboard.tsx      # Summary cards and analytics
│   ├── ExpenseForm.tsx    # Add/edit expense form with validation
│   ├── ExpenseList.tsx    # Expense list with filters
│   ├── ExpenseItem.tsx    # Individual expense display
│   ├── SpendingChart.tsx  # Visual spending breakdown
│   └── Modal.tsx          # Reusable modal component
├── contexts/              # React contexts
│   └── ExpenseContext.tsx # Global expense state management
├── lib/                   # Utility functions
│   ├── localStorage.ts    # localStorage operations
│   └── utils.ts           # Helper functions (formatting, calculations)
└── types/                 # TypeScript definitions
    └── expense.ts         # Expense-related type definitions
```

### Key Concepts

**State Management**: The application uses React Context API via `ExpenseContext` to manage global expense state. All expense operations (add, update, delete) are handled through this context and persisted to localStorage.

**Data Persistence**: All expense data is stored in browser localStorage under the key `expense-tracker-data`. Data is automatically loaded on mount and saved on every change.

**Component Architecture**:
- The main `page.tsx` orchestrates three views (Dashboard, Expenses, Add) via tab navigation
- `ExpenseContext` provides expense data and CRUD operations to all components
- Components are client-side (`'use client'`) due to browser APIs (localStorage) and interactivity

**Type Safety**: All data structures are strictly typed in `types/expense.ts`:
- `Expense`: Complete expense record with metadata
- `ExpenseFormData`: Form input shape
- `ExpenseFilters`: Filter criteria for expense list
- `Category`: Union type of expense categories

### Features Implementation

1. **Dashboard**: Displays summary cards (total spending, monthly spending, expense count, top category) and category breakdown with visual progress bars

2. **Expense Management**:
   - Add new expenses with validation
   - Edit existing expenses via modal
   - Delete expenses with confirmation dialog
   - All fields validated: date, amount (must be > 0), category, description (max 200 chars)

3. **Filtering & Search**:
   - Text search across description, category, and amount
   - Filter by category
   - Filter by date range (start/end dates)
   - Results show filtered count and total

4. **Data Export**: CSV export functionality generates downloadable file with all expense data

5. **Visual Analytics**: Bar chart showing spending by category with percentages and color-coded categories

### Category Colors

Each expense category has a consistent color scheme defined in `lib/utils.ts`:
- Food: Green
- Transportation: Blue
- Entertainment: Purple
- Shopping: Pink
- Bills: Red
- Other: Gray

### Form Validation

The `ExpenseForm` component implements comprehensive validation:
- Real-time validation on blur
- All fields required
- Amount must be positive number
- Description limited to 200 characters
- Date cannot be in future
- Error messages displayed below fields

## Common Development Tasks

### Adding a New Category

1. Update the `Category` type in `types/expense.ts`
2. Add color mapping in `getCategoryColor()` and `getCategoryTextColor()` in `lib/utils.ts`
3. Add to `categoryBreakdown` initialization in `calculateSummary()` in `lib/utils.ts`

### Modifying Expense Schema

1. Update the `Expense` interface in `types/expense.ts`
2. Update localStorage operations in `lib/localStorage.ts` if needed
3. Update form fields in `components/ExpenseForm.tsx`
4. Update display in `components/ExpenseItem.tsx`

### Changing Data Persistence

Currently uses localStorage. To switch to a backend API:
1. Replace localStorage operations in `lib/localStorage.ts` with API calls
2. Add loading states and error handling in `ExpenseContext.tsx`
3. Consider adding optimistic updates for better UX

## Browser Compatibility

The application uses modern browser APIs:
- localStorage (required)
- ES6+ JavaScript features
- CSS Grid and Flexbox

Recommended browsers: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
