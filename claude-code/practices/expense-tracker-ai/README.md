# 💰 Expense Tracker

A modern, professional expense tracking web application built with Next.js 14, TypeScript, and Tailwind CSS. Track your personal finances with an intuitive interface, powerful filtering, and visual analytics.

![Next.js](https://img.shields.io/badge/Next.js-14-black)
![TypeScript](https://img.shields.io/badge/TypeScript-5-blue)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3-38bdf8)

## ✨ Features

### 📊 Dashboard
- **Summary Cards**: View total spending, monthly spending, expense count, and top category at a glance
- **Category Breakdown**: Visual breakdown of spending by category with percentages
- **Spending Chart**: Bar chart showing spending distribution across categories

### 💸 Expense Management
- **Add Expenses**: Easy-to-use form with real-time validation
- **Edit Expenses**: Update expense details via modal dialog
- **Delete Expenses**: Remove expenses with confirmation dialog
- **Form Validation**: Comprehensive validation for all fields
  - Date (required, cannot be in future)
  - Amount (required, must be positive)
  - Category (6 predefined categories)
  - Description (required, max 200 characters)

### 🔍 Advanced Filtering
- **Text Search**: Search across description, category, and amount
- **Category Filter**: Filter by specific category
- **Date Range Filter**: Filter expenses by start and end dates
- **Results Summary**: See filtered count and total amount
- **Clear Filters**: Reset all filters with one click

### 📈 Analytics
- **Total Spending**: All-time spending summary
- **Monthly Spending**: Current month's expenses
- **Top Category**: See which category you spend most on
- **Visual Charts**: Color-coded bar charts and distribution views

### 💾 Data Export
- **CSV Export**: Download all expenses as CSV file for external analysis
- **Formatted Data**: Properly formatted dates, categories, amounts, and descriptions

### 📱 Responsive Design
- **Mobile-First**: Optimized for mobile devices
- **Tablet Support**: Adapts to tablet screens
- **Desktop Layout**: Full-featured desktop experience
- **Touch-Friendly**: Large tap targets and intuitive gestures

### 🎨 Modern UI
- **Clean Design**: Professional, minimalist interface
- **Color-Coded Categories**: Each category has a unique color
- **Smooth Animations**: Subtle transitions and loading states
- **Accessibility**: Keyboard navigation and screen reader support

## 🚀 Getting Started

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Run the development server**
   ```bash
   npm run dev
   ```

3. **Open your browser**

   Navigate to [http://localhost:3000](http://localhost:3000)

### Building for Production

```bash
# Create production build
npm run build

# Start production server
npm start
```

## 📖 Usage Guide

### Adding an Expense

1. Click the **"Add Expense"** tab
2. Fill in the expense details:
   - **Date**: When the expense occurred (defaults to today)
   - **Amount**: How much you spent (must be positive)
   - **Category**: Choose from Food, Transportation, Entertainment, Shopping, Bills, or Other
   - **Description**: Brief description of the expense
3. Click **"Add Expense"** to save

### Viewing Expenses

1. Go to the **"Dashboard"** tab to see:
   - Summary cards with key metrics
   - Category breakdown chart
   - Spending distribution

2. Go to the **"Expenses"** tab to see:
   - Complete list of all expenses
   - Search and filter options
   - Edit and delete buttons for each expense

### Filtering Expenses

In the **"Expenses"** tab:
1. **Search**: Type in the search box to filter by description, category, or amount
2. **Category**: Select a specific category from the dropdown
3. **Date Range**: Set start and/or end dates to filter by date
4. **Clear**: Click "Clear All" to reset filters

### Editing an Expense

1. Find the expense in the **"Expenses"** tab
2. Click the **edit icon** (pencil)
3. Update the fields in the modal
4. Click **"Update Expense"** to save changes
5. Click **"Cancel"** to discard changes

### Deleting an Expense

1. Find the expense in the **"Expenses"** tab
2. Click the **delete icon** (trash can)
3. Confirm deletion in the dialog
4. The expense will be permanently removed

### Exporting Data

1. Click the **"Export CSV"** button in the header (appears when you have expenses)
2. A CSV file will be downloaded with all your expense data
3. Open it in Excel, Google Sheets, or any spreadsheet application

## 🎨 Expense Categories

The app includes 6 predefined categories, each with a unique color:

- 🍔 **Food** (Green): Groceries, restaurants, meals
- 🚗 **Transportation** (Blue): Gas, public transit, parking
- 🎮 **Entertainment** (Purple): Movies, games, hobbies
- 🛍️ **Shopping** (Pink): Clothes, electronics, household items
- 💳 **Bills** (Red): Utilities, subscriptions, rent
- 📦 **Other** (Gray): Everything else

## 🔧 Technical Details

### Tech Stack

- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: React Context API
- **Data Storage**: Browser localStorage
- **Font**: Inter (Google Fonts)

### Project Structure

```
├── app/                    # Next.js app directory
│   ├── layout.tsx         # Root layout
│   ├── page.tsx           # Main page
│   └── globals.css        # Global styles
├── components/            # React components
│   ├── Dashboard.tsx
│   ├── ExpenseForm.tsx
│   ├── ExpenseList.tsx
│   ├── ExpenseItem.tsx
│   ├── SpendingChart.tsx
│   └── Modal.tsx
├── contexts/              # React contexts
│   └── ExpenseContext.tsx
├── lib/                   # Utilities
│   ├── localStorage.ts
│   └── utils.ts
└── types/                 # TypeScript types
    └── expense.ts
```

### Data Persistence

All expense data is stored in your browser's localStorage. This means:
- ✅ No server required
- ✅ Data stays on your device
- ✅ Fast and responsive
- ⚠️ Data is per-browser (clearing browser data will delete expenses)
- ⚠️ Not synced across devices

To back up your data, use the CSV export feature regularly.

## 🎯 Features to Test

### Basic Functionality
- [ ] Add a new expense
- [ ] View expense in the list
- [ ] Edit an existing expense
- [ ] Delete an expense
- [ ] View dashboard metrics

### Filtering
- [ ] Search for expenses by description
- [ ] Filter by category
- [ ] Filter by date range
- [ ] Use multiple filters together
- [ ] Clear all filters

### Data Export
- [ ] Export expenses to CSV
- [ ] Open CSV file and verify data

### Validation
- [ ] Try to submit empty form (should show errors)
- [ ] Try negative amount (should show error)
- [ ] Try description over 200 characters (should show error)
- [ ] Try future date (should be limited to today)

### UI/UX
- [ ] Test on mobile device
- [ ] Test on tablet
- [ ] Test keyboard navigation
- [ ] Check animations and transitions

## 🌐 Browser Support

Tested and working on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📝 License

This project is open source and available for personal use.

## 🤝 Contributing

This is a demo application. Feel free to fork and customize for your needs!

## 💡 Future Enhancements

Potential features to add:
- 🔐 User authentication
- ☁️ Cloud sync across devices
- 📊 More chart types (pie charts, line graphs)
- 🏷️ Custom categories
- 💰 Budget limits and alerts
- 📅 Recurring expenses
- 🌍 Multi-currency support
- 📸 Receipt photo uploads
- 📤 Export to PDF
- 📊 Advanced reporting

---

Built with ❤️ using Next.js 14
