// src/lib/deps.ts
// هدف: همه importها یک‌دست از یک فایل انجام شود.
// توجه: ممکن است برخی پکیج‌ها default export داشته باشند؛ در آن صورت wrapper/alias اضافه کنید.

export { useEffect, useMemo, useState, useCallback } from "react";
export { View, Text, Pressable, TextInput, Image, ScrollView } from "react-native";

export { Stack, Tabs, router } from "expo-router";

// Uncomment these after you install the packages:
// export * as Notifications from "expo-notifications";
// export * as ImagePicker from "expo-image-picker";
// export * as FileSystem from "expo-file-system";
// export * as SQLite from "expo-sqlite";

export { create } from "zustand";
