# Project: FitnessTracker Mobile App

## Platform Requirements
- **Framework**: React Native 0.72+ with TypeScript
- **State Management**: Redux Toolkit with RTK Query
- **Navigation**: React Navigation v6
- **UI Library**: Native Base for consistent design
- **Platform Support**: iOS 14+ and Android API 24+

## Branch Strategy
1. Create feature branches: `mobile-[feature-name]`
2. Use conventional commits: `feat:`, `fix:`, `refactor:`, etc.
3. Test on both iOS and Android before committing
4. Run `npm run lint` and `npm run type-check` before commits

## Code Organization
- **Screens**: `/src/screens/[FeatureName]/[ScreenName]Screen.tsx`
- **Components**: `/src/components/[ComponentName]/index.tsx`
- **Navigation**: `/src/navigation/[NavigatorName]Navigator.tsx`
- **Services**: `/src/services/[serviceName].ts`
- **Store**: `/src/store/slices/[featureName]Slice.ts`

## Mobile-Specific Standards
- Use React Native's built-in components before third-party libraries
- Implement proper error boundaries for crash prevention
- Use AsyncStorage for local data persistence
- Follow platform-specific design guidelines (iOS Human Interface, Material Design)
- Optimize images and use vector graphics when possible

## Testing Requirements
- Unit tests with Jest and React Native Testing Library
- E2E tests with Detox for critical user flows
- Test on physical devices before major releases
- Performance testing with Flipper profiling

## Performance Guidelines
- Use FlatList for large datasets, never ScrollView
- Implement proper memoization with React.memo and useMemo
- Lazy load heavy components and screens
- Monitor bundle size and use code splitting when necessary