#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create the full Todo Smart app folder structure + placeholder files (Expo/React Native oriented)
Run:
  python create_structure.py
Optional:
  python create_structure.py --root todo-smart
"""

from __future__ import annotations
import argparse
from pathlib import Path
from datetime import datetime

# -------------------------
# Helpers
# -------------------------
def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, content: str, overwrite: bool = False) -> None:
    ensure_dir(path.parent)
    if path.exists() and not overwrite:
        return
    path.write_text(content, encoding="utf-8")

def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")

# -------------------------
# File contents (templates)
# -------------------------
README = f"""# Todo Smart (فارسی) — ساختار پروژه
ایجاد شده در: {now_stamp()}

## اجرا (بعداً)
این ساختار برای Expo/React Native آماده شده و شامل:
- specs/ (PRD، Flow، Rules، Tasks به فارسی)
- apps/mobile/ (اسکلت اپ)
- design tokens (رنگ/فونت/فاصله بدون hardcode)
- deps.ts برای یکپارچه‌سازی importها

> نکته: اینجا فقط ساختار و فایل‌های پایه ساخته می‌شود. نصب پکیج‌ها و اجرای Expo مرحله بعدی است.
"""

PRD_FA = """# PRD — اپ لیست کارها (Todo Smart) [فارسی]

## هدف محصول
یک اپ مدیریت کارها که علاوه بر CRUD وظایف و یادآوری، تحلیل و گزارش‌های روزانه/هفتگی/ماهانه ارائه می‌دهد
و سختی/آسانی کارها را بر اساس تلاش‌ها و زمان صرف‌شده تشخیص می‌دهد.

## ویژگی‌ها (خلاصه)
1) افزودن/حذف/ویرایش وظیفه: عنوان، ددلاین، توضیح، مدیا (عکس/ویدئو)، سطح اهمیت
2) یادآوری با گزینه‌های: 1 ساعت، 5 ساعت، 1 روز، 2 روز (انتخاب کاربر)
3) وضعیت: انجام‌شده / انجام‌نشده / به‌تعویق‌افتاده
4) گزارش‌ها: پایان روز، آخر هفته، پایان ماه (نمودار و دیاگرام)
5) تغییر زمان‌بندی (Reschedule) + یادآوری زمان جدید
6) تشخیص سخت/آسان بر اساس تعداد تلاش و زمان صرف‌شده

## معیارهای موفقیت
- افزایش نرخ انجام (Done rate)
- کاهش وظایف به تعویق افتاده
- تعامل با نوتیف‌ها
"""

PHASES_FA = """# فازهای توسعه (Roadmap) — فارسی

## فاز 1: MVP
- CRUD وظایف
- ددلاین + یادآوری (نوتیف)
- وضعیت‌ها (Done/Not Done/Delayed)
- خلاصه روزانه ساده

## فاز 2: آنالیتیکس و گزارش
- نمودارهای روزانه/هفتگی/ماهانه
- ذخیره زمان صرف‌شده
- محاسبه سختی/آسانی

## فاز 3: هوشمندسازی
- پیشنهادهای بهره‌وری
- پیش‌بینی سختی (اختیاری)
- خروجی گزارش (PDF) (اختیاری)
"""

UI_RULES_FA = """# قوانین UI (فارسی) — Todo Smart

## 1) اصول کلی
- هدف UI: شاد، سبک، مینیمال، قابل فهم
- حس کلی: Happy vibes با رنگ‌های پاستلی (آبی/صورتی/مرجانی)
- زبان اپ: فارسی (RTL)

## 2) سیستم رنگ
- Primary: پاستلی آبی
- Secondary: پاستلی صورتی
- Accent: مرجانی/قرمز پاستلی برای تاکید و اهمیت
- Background: سفید/خیلی روشن
- استفاده از رنگ فقط از design tokens مجاز است
- Hardcode رنگ داخل کامپوننت‌ها ممنوع

## 3) تایپوگرافی
- فونت فارسی استاندارد (مثلاً Vazirmatn یا IRANSansX)
- Title: بزرگ و واضح
- Body: خوانا با line-height مناسب
- Hardcode فونت/سایز ممنوع (فقط tokens)

## 4) شکل‌ها و کامپوننت‌ها
- گوشه‌ها Rounded برای کارت/دکمه/مودال
- سایه نرم
- Badge وضعیت با رنگ‌های ملایم

## 5) فاصله‌گذاری
- سیستم فاصله 8pt (فقط spacing tokens)
- UI خلوت و بدون شلوغی

## 6) کارت وظیفه
- عنوان، زمان ددلاین، نشانگر اهمیت، badge وضعیت
- دسترسی سریع به Edit/Delete

## 7) صفحه افزودن/ویرایش
- فرم ساده
- انتخاب مدیا با preview
- Reminder: 1 ساعت، 5 ساعت، 1 روز، 2 روز
- دکمه ذخیره واضح و در دسترس

## 8) آنالیتیکس
- نمودارهای ساده
- پیام‌های کوتاه تشویقی فارسی

## 9) ممنوعیت‌ها
- Hardcode رنگ/فونت/spacing ممنوع
- شلوغی و کنتراست آزاردهنده ممنوع
"""

# Flow placeholders
FLOW_ONBOARDING = """# Flow: آنبوردینگ (Onboarding) — فارسی
## هدف
کاربر را با قابلیت‌های اپ آشنا کند و دسترسی نوتیفیکیشن را بگیرد.

## مراحل
1) اسپلش
2) کارت‌های معرفی ویژگی‌ها
3) درخواست Permission نوتیفیکیشن
4) ورود به صفحه خانه
"""

FLOW_HOME = """# Flow: خانه (Home / Task List) — فارسی
## هدف
نمایش لیست وظایف، فیلترها، وضعیت‌ها، و دسترسی سریع به افزودن وظیفه.

## مراحل
1) نمایش سلام + تاریخ
2) نمایش Progress امروز
3) لیست کارت‌های وظیفه
4) اکشن‌ها: Add، Edit، Delete، تغییر وضعیت
"""

FLOW_CREATE_TASK = """# Flow: ایجاد/ویرایش وظیفه (Create/Edit Task) — فارسی
## هدف
کاربر بتواند وظیفه با عنوان، ددلاین، توضیح، مدیا، اهمیت و Reminder بسازد.

## مراحل
1) ورود به فرم
2) وارد کردن Title
3) انتخاب Deadline (date+time)
4) Description (اختیاری)
5) Attach media (اختیاری)
6) انتخاب Importance (Low/Medium/High/Critical)
7) انتخاب Reminder options (1h, 5h, 1d, 2d)
8) Save
9) بازگشت به Home + زمان‌بندی نوتیف‌ها
"""

FLOW_TASK_DETAIL = """# Flow: جزئیات وظیفه (Task Detail) — فارسی
## هدف
نمایش جزئیات کامل وظیفه و اکشن‌های Done/Delay/Edit.

## مراحل
1) نمایش عنوان و ددلاین (Countdown)
2) نمایش توضیح و مدیا
3) اکشن‌ها: Done / Delay-Reschedule / Edit
"""

FLOW_REMINDER = """# Flow: یادآوری (Reminder) — فارسی
## هدف
ارسال نوتیف در زمان‌های انتخاب‌شده و ارائه اکشن سریع.

## مراحل
1) ارسال Notification
2) اکشن‌های سریع: Mark Done / Delay / Open Task
3) در Delay: رفتن به Reschedule
"""

FLOW_ANALYTICS = """# Flow: آنالیتیکس (Analytics) — فارسی
## هدف
نمایش نمودارها و خلاصه‌های روزانه/هفتگی/ماهانه.

## مراحل
1) نمایش Pie (Done/Not Done/Delayed)
2) نمایش Bar/Line برای روند
3) بخش سخت/آسان
4) پیام تشویقی فارسی
"""

# Rules placeholders
TASK_RULES = """# Rules: وظیفه (Task) — فارسی
- هر Task باید title داشته باشد.
- deadline اختیاری نیست (برای MVP پیشنهاد: اجباری باشد).
- media اختیاری است.
- importance یکی از: Low/Medium/High/Critical
"""

REMINDER_RULES = """# Rules: یادآوری (Reminder) — فارسی
- Reminderها فقط از گزینه‌های تعریف‌شده انتخاب می‌شوند: 1h, 5h, 1d, 2d
- اگر Task reschedule شد:
  - Reminderهای قبلی لغو شوند
  - Reminderهای جدید بر اساس deadline جدید ساخته شوند
"""

STATUS_RULES = """# Rules: وضعیت‌ها (Status) — فارسی
- وضعیت‌ها: Done / Not Done / Delayed
- اگر زمان فعلی از deadline عبور کند و Done نشده باشد => Delayed (طبق سیاست محصول)
"""

ANALYTICS_RULES = """# Rules: آنالیتیکس — فارسی
- گزارش روزانه پایان روز: تعداد Done/Not Done/Delayed
- گزارش هفتگی: روند 7 روز
- گزارش ماهانه: روند و نرخ‌ها
"""

DIFFICULTY_RULES = """# Rules: سختی/آسانی (Difficulty) — فارسی
- معیارها:
  - attempt_count
  - reschedule_count
  - total_time_spent
- مثال:
  - Easy: attempt<=1 و reschedule==0 و time_spent پایین
  - Medium: attempt 2-3 یا reschedule 1
  - Hard: attempt>=3 یا reschedule>=2 یا time_spent بالا
"""

# Tasks placeholders
MVP_TASKS = """# Tasks: MVP — فارسی
- [ ] ساخت ساختار دیتابیس Task
- [ ] صفحه Home (لیست وظایف)
- [ ] صفحه Create/Edit Task
- [ ] ذخیره Task در SQLite
- [ ] تغییر وضعیت Task (Done/Not Done/Delayed)
- [ ] زمان‌بندی Notification بر اساس Reminder options
"""

NOTIF_TASKS = """# Tasks: Notifications — فارسی
- [ ] درخواست Permission نوتیفیکیشن
- [ ] زمان‌بندی نوتیف‌ها برای هر Task
- [ ] لغو و ساخت مجدد در Reschedule
- [ ] اکشن‌های سریع (Mark Done / Delay / Open)
"""

ANALYTICS_TASKS = """# Tasks: Analytics — فارسی
- [ ] محاسبه خلاصه روزانه/هفتگی/ماهانه
- [ ] ذخیره و بروزرسانی آمار
- [ ] نمایش نمودارها در UI
"""

MEDIA_TASKS = """# Tasks: Media — فارسی
- [ ] انتخاب عکس/ویدئو
- [ ] ذخیره URI و preview در Task
- [ ] مدیریت دسترسی‌ها
"""

# Expo Router placeholders
LAYOUT_TSX = """import { Stack } from "expo-router";

export default function RootLayout() {
  return (
    <Stack screenOptions={{ headerShown: false }}>
      <Stack.Screen name="(tabs)" />
      <Stack.Screen name="task/new" />
      <Stack.Screen name="task/[id]" />
    </Stack>
  );
}
"""

TABS_LAYOUT = """import { Tabs } from "expo-router";

export default function TabsLayout() {
  return (
    <Tabs screenOptions={{ headerShown: false }}>
      <Tabs.Screen name="index" options={{ title: "خانه" }} />
      <Tabs.Screen name="analytics" options={{ title: "گزارش‌ها" }} />
      <Tabs.Screen name="settings" options={{ title: "تنظیمات" }} />
    </Tabs>
  );
}
"""

HOME_SCREEN = """import { View, Text, Pressable } from "@/lib/deps";
import { theme } from "@/design/theme";

export default function HomeScreen() {
  return (
    <View style={{ flex: 1, backgroundColor: theme.colors.bg, padding: theme.spacing.md }}>
      <Text style={{ fontFamily: theme.typography.fontFamily.bold, fontSize: theme.typography.size.xl, color: theme.colors.text }}>
        سلام 👋
      </Text>

      <Text style={{ marginTop: theme.spacing.sm, color: theme.colors.textMuted }}>
        لیست کارها اینجا نمایش داده می‌شود.
      </Text>

      <Pressable
        style={{
          marginTop: theme.spacing.lg,
          paddingVertical: theme.spacing.sm,
          borderRadius: theme.radius.lg,
          backgroundColor: theme.colors.primary,
          alignItems: "center",
        }}
        onPress={() => {}}
      >
        <Text style={{ fontFamily: theme.typography.fontFamily.medium, color: theme.colors.text }}>
          + افزودن وظیفه
        </Text>
      </Pressable>
    </View>
  );
}
"""

ANALYTICS_SCREEN = """import { View, Text } from "@/lib/deps";
import { theme } from "@/design/theme";

export default function AnalyticsScreen() {
  return (
    <View style={{ flex: 1, backgroundColor: theme.colors.bg, padding: theme.spacing.md }}>
      <Text style={{ fontFamily: theme.typography.fontFamily.bold, fontSize: theme.typography.size.xl, color: theme.colors.text }}>
        گزارش‌ها
      </Text>
      <Text style={{ marginTop: theme.spacing.sm, color: theme.colors.textMuted }}>
        نمودارها و خلاصه‌ها اینجا نمایش داده می‌شود.
      </Text>
    </View>
  );
}
"""

SETTINGS_SCREEN = """import { View, Text } from "@/lib/deps";
import { theme } from "@/design/theme";

export default function SettingsScreen() {
  return (
    <View style={{ flex: 1, backgroundColor: theme.colors.bg, padding: theme.spacing.md }}>
      <Text style={{ fontFamily: theme.typography.fontFamily.bold, fontSize: theme.typography.size.xl, color: theme.colors.text }}>
        تنظیمات
      </Text>
      <Text style={{ marginTop: theme.spacing.sm, color: theme.colors.textMuted }}>
        تنظیمات نوتیفیکیشن و اپ اینجا خواهد بود.
      </Text>
    </View>
  );
}
"""

TASK_NEW = """import { View, Text } from "@/lib/deps";
import { theme } from "@/design/theme";

export default function NewTaskScreen() {
  return (
    <View style={{ flex: 1, backgroundColor: theme.colors.bg, padding: theme.spacing.md }}>
      <Text style={{ fontFamily: theme.typography.fontFamily.bold, fontSize: theme.typography.size.xl, color: theme.colors.text }}>
        افزودن وظیفه
      </Text>
      <Text style={{ marginTop: theme.spacing.sm, color: theme.colors.textMuted }}>
        فرم ایجاد وظیفه اینجا ساخته می‌شود.
      </Text>
    </View>
  );
}
"""

TASK_DETAIL = """import { View, Text } from "@/lib/deps";
import { theme } from "@/design/theme";

export default function TaskDetailScreen() {
  return (
    <View style={{ flex: 1, backgroundColor: theme.colors.bg, padding: theme.spacing.md }}>
      <Text style={{ fontFamily: theme.typography.fontFamily.bold, fontSize: theme.typography.size.xl, color: theme.colors.text }}>
        جزئیات وظیفه
      </Text>
      <Text style={{ marginTop: theme.spacing.sm, color: theme.colors.textMuted }}>
        جزئیات وظیفه با شناسه‌ی مسیر اینجا نمایش داده می‌شود.
      </Text>
    </View>
  );
}
"""

# Design tokens
COLORS_TS = """export const colors = {
  bg: "#FFFFFF",
  surface: "#F7F8FF",

  primary: "#A8D8FF",   // pastel blue
  secondary: "#FFC7E6", // pastel pink
  accent: "#FF9AA2",    // pastel red/coral

  text: "#1F2430",
  textMuted: "#6B7280",

  success: "#A7F3D0",
  warning: "#FDE68A",
  danger: "#FCA5A5",
} as const;
"""

TYPOGRAPHY_TS = """export const typography = {
  fontFamily: {
    regular: "Vazirmatn-Regular",
    medium: "Vazirmatn-Medium",
    bold: "Vazirmatn-Bold",
  },
  size: {
    xs: 12,
    sm: 14,
    md: 16,
    lg: 20,
    xl: 24,
  },
  lineHeight: {
    md: 22,
    lg: 28,
  },
} as const;
"""

SPACING_TS = """export const spacing = {
  xxs: 4,
  xs: 8,
  sm: 12,
  md: 16,
  lg: 20,
  xl: 24,
  xxl: 32,
} as const;
"""

RADIUS_TS = """export const radius = {
  sm: 10,
  md: 14,
  lg: 18,
  xl: 24,
} as const;
"""

SHADOWS_TS = """export const shadows = {
  card: {
    shadowColor: "#000",
    shadowOpacity: 0.06,
    shadowRadius: 10,
    shadowOffset: { width: 0, height: 4 },
    elevation: 2,
  },
} as const;
"""

THEME_TS = """import { colors } from "./tokens/colors";
import { spacing } from "./tokens/spacing";
import { typography } from "./tokens/typography";
import { radius } from "./tokens/radius";
import { shadows } from "./tokens/shadows";

export const theme = { colors, spacing, typography, radius, shadows };
export type Theme = typeof theme;
"""

# deps.ts aggregator
DEPS_TS = """// src/lib/deps.ts
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
"""

# Minimal config placeholders
ENV_TS = """export const env = {
  APP_NAME: "Todo Smart",
} as const;
"""

APP_CONFIG_TS = """import { env } from "./env";

export const appConfig = {
  name: env.APP_NAME,
  locale: "fa-IR",
  direction: "rtl",
} as const;
"""

I18N_TS = """// فعلاً همه چیز فارسی است.
// اگر بعداً نیاز به چندزبانه شد، از همینجا مدیریت می‌کنیم.
export const i18n = {
  locale: "fa-IR",
  direction: "rtl" as const,
};
"""

BOOT_PLACEHOLDER = """// اینجا initها انجام می‌شود: فونت، دیتابیس، نوتیفیکیشن، ...
// برای MVP می‌توان بعداً اضافه کرد.
export function boot() {
  // TODO: load fonts
  // TODO: init db
  // TODO: init notifications
}
"""

PACKAGE_JSON = """{
  "name": "todo-smart-mobile",
  "private": true,
  "version": "0.1.0",
  "main": "expo-router/entry",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web"
  },
  "dependencies": {
    "expo": "^51.0.0",
    "expo-router": "^3.5.0",
    "react": "18.2.0",
    "react-native": "0.74.0",
    "zustand": "^4.5.2"
  }
}
"""

APP_JSON = """{
  "expo": {
    "name": "Todo Smart",
    "slug": "todo-smart",
    "scheme": "todo-smart",
    "plugins": ["expo-router"],
    "extra": {}
  }
}
"""

# -------------------------
# Structure definition
# -------------------------
def build_structure(root: Path) -> dict[Path, str]:
    return {
        root / "README.md": README,

        # Specs (فارسی)
        root / "specs" / "prd.fa.md": PRD_FA,
        root / "specs" / "phases.fa.md": PHASES_FA,

        root / "specs" / "flow" / "01-onboarding.flow.fa.md": FLOW_ONBOARDING,
        root / "specs" / "flow" / "02-home.flow.fa.md": FLOW_HOME,
        root / "specs" / "flow" / "03-create-task.flow.fa.md": FLOW_CREATE_TASK,
        root / "specs" / "flow" / "04-task-detail.flow.fa.md": FLOW_TASK_DETAIL,
        root / "specs" / "flow" / "05-reminder.flow.fa.md": FLOW_REMINDER,
        root / "specs" / "flow" / "06-analytics.flow.fa.md": FLOW_ANALYTICS,

        root / "specs" / "rules" / "ui.rules.fa.md": UI_RULES_FA,
        root / "specs" / "rules" / "task.rules.fa.md": TASK_RULES,
        root / "specs" / "rules" / "reminder.rules.fa.md": REMINDER_RULES,
        root / "specs" / "rules" / "status.rules.fa.md": STATUS_RULES,
        root / "specs" / "rules" / "analytics.rules.fa.md": ANALYTICS_RULES,
        root / "specs" / "rules" / "difficulty.rules.fa.md": DIFFICULTY_RULES,

        root / "specs" / "tasks" / "mvp.tasks.fa.md": MVP_TASKS,
        root / "specs" / "tasks" / "notifications.tasks.fa.md": NOTIF_TASKS,
        root / "specs" / "tasks" / "analytics.tasks.fa.md": ANALYTICS_TASKS,
        root / "specs" / "tasks" / "media.tasks.fa.md": MEDIA_TASKS,

        # Mobile app skeleton
        root / "apps" / "mobile" / "package.json": PACKAGE_JSON,
        root / "apps" / "mobile" / "app.json": APP_JSON,

        # Expo Router routes
        root / "apps" / "mobile" / "app" / "_layout.tsx": LAYOUT_TSX,
        root / "apps" / "mobile" / "app" / "(tabs)" / "_layout.tsx": TABS_LAYOUT,
        root / "apps" / "mobile" / "app" / "(tabs)" / "index.tsx": HOME_SCREEN,
        root / "apps" / "mobile" / "app" / "(tabs)" / "analytics.tsx": ANALYTICS_SCREEN,
        root / "apps" / "mobile" / "app" / "(tabs)" / "settings.tsx": SETTINGS_SCREEN,
        root / "apps" / "mobile" / "app" / "task" / "new.tsx": TASK_NEW,
        root / "apps" / "mobile" / "app" / "task" / "[id].tsx": TASK_DETAIL,

        # src folders & core files
        root / "apps" / "mobile" / "src" / "boot" / "boot.ts": BOOT_PLACEHOLDER,
        root / "apps" / "mobile" / "src" / "config" / "env.ts": ENV_TS,
        root / "apps" / "mobile" / "src" / "config" / "app.ts": APP_CONFIG_TS,

        root / "apps" / "mobile" / "src" / "lib" / "deps.ts": DEPS_TS,
        root / "apps" / "mobile" / "src" / "lib" / "i18n.ts": I18N_TS,

        # design system
        root / "apps" / "mobile" / "src" / "design" / "theme.ts": THEME_TS,
        root / "apps" / "mobile" / "src" / "design" / "ui-rules.fa.md": UI_RULES_FA,
        root / "apps" / "mobile" / "src" / "design" / "tokens" / "colors.ts": COLORS_TS,
        root / "apps" / "mobile" / "src" / "design" / "tokens" / "typography.ts": TYPOGRAPHY_TS,
        root / "apps" / "mobile" / "src" / "design" / "tokens" / "spacing.ts": SPACING_TS,
        root / "apps" / "mobile" / "src" / "design" / "tokens" / "radius.ts": RADIUS_TS,
        root / "apps" / "mobile" / "src" / "design" / "tokens" / "shadows.ts": SHADOWS_TS,

        # Placeholder directories (keep as .gitkeep)
        root / "apps" / "mobile" / "src" / "domain" / ".gitkeep": "",
        root / "apps" / "mobile" / "src" / "data" / ".gitkeep": "",
        root / "apps" / "mobile" / "src" / "state" / ".gitkeep": "",
        root / "apps" / "mobile" / "src" / "components" / ".gitkeep": "",
        root / "apps" / "mobile" / "src" / "assets" / "fonts" / ".gitkeep": "",
    }

def ensure_empty_dirs(root: Path) -> None:
    # Extra dirs that might be useful
    extra_dirs = [
        root / "apps" / "mobile" / "src" / "data" / "db",
        root / "apps" / "mobile" / "src" / "data" / "notifications",
        root / "apps" / "mobile" / "src" / "data" / "repositories",
        root / "apps" / "mobile" / "src" / "domain" / "entities",
        root / "apps" / "mobile" / "src" / "domain" / "rules",
        root / "apps" / "mobile" / "src" / "domain" / "usecases",
    ]
    for d in extra_dirs:
        ensure_dir(d)
        write_file(d / ".gitkeep", "")

# -------------------------
# Main
# -------------------------
def main() -> None:
    parser = argparse.ArgumentParser(description="Create Todo Smart structure + files.")
    parser.add_argument("--root", default="todo-smart", help="Root folder name/path to create.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    ensure_dir(root)

    files = build_structure(root)

    created, skipped = 0, 0
    for path, content in files.items():
        before = path.exists()
        write_file(path, content, overwrite=args.overwrite)
        after = path.exists()
        # Count only if file was newly created or overwritten intentionally
        if not before and after:
            created += 1
        elif before and not args.overwrite:
            skipped += 1

    ensure_empty_dirs(root)

    print("✅ Done!")
    print(f"Root: {root}")
    print(f"Files created: {created}")
    if skipped:
        print(f"Files skipped (already existed): {skipped}")
    if args.overwrite:
        print("Overwrite: ON")

if __name__ == "__main__":
    main()
