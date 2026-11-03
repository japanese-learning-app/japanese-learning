# -*- coding: utf-8 -*-
"""
JLPT 聴解用 高品質 4:3 ベクターSVGイラスト生成エンジン
全レベル（N5〜N1）の全聴解問題に対応する場面イラスト、4分割図、発話矢印図を生成
"""

import os
import html

def make_scene_svg(title, category, speaker_a="女性", speaker_b="男性", details=""):
    """
    シチュエーション場面イラスト (4:3 ratio: 400x300)
    """
    # Background color palette based on category
    bg_colors = {
        "オフィス": ("#F0FDF4", "#DCFCE7", "#166534"),
        "学校・教室": ("#EFF6FF", "#DBEAFE", "#1E40AF"),
        "店・買い物": ("#FFFBEB", "#FEF3C7", "#92400E"),
        "駅・移動": ("#F5F3FF", "#EDE9FE", "#5B21B6"),
        "家庭・日常": ("#FFF1F2", "#FFE4E6", "#9F1239"),
        "病院・施設": ("#ECFEFF", "#CFFAFE", "#155E75"),
        "一般": ("#F8FAFC", "#F1F5F9", "#334155")
    }
    bg_c, box_c, text_c = bg_colors.get(category, bg_colors["一般"])
    
    clean_title = html.escape(title)
    clean_details = html.escape(details)
    clean_sp_a = html.escape(speaker_a)
    clean_sp_b = html.escape(speaker_b)
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg_c}" />
      <stop offset="100%" stop-color="{box_c}" />
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.08" />
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="400" height="300" rx="16" fill="url(#bgGrad)" stroke="#E2E8F0" stroke-width="1.5" />

  <!-- Category Tag -->
  <rect x="20" y="16" width="90" height="24" rx="12" fill="{text_c}" />
  <text x="65" y="32" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">{category}</text>

  <!-- Title Banner -->
  <text x="120" y="33" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#1E293B">{clean_title}</text>

  <!-- Main Scene Area (Room / Environment) -->
  <g transform="translate(30, 56)">
    <!-- Room Floor / Desk -->
    <rect x="0" y="0" width="340" height="175" rx="12" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" filter="url(#shadow)" />
    
    <!-- Interior Furniture / Setting Line -->
    <line x1="20" y1="130" x2="320" y2="130" stroke="#E2E8F0" stroke-width="2" stroke-dasharray="4 4" />
    
    <!-- Speaker A (Left) -->
    <g transform="translate(60, 40)">
      <!-- Head -->
      <circle cx="30" cy="30" r="22" fill="#FDE047" stroke="#334155" stroke-width="2" />
      <circle cx="23" cy="28" r="2.5" fill="#334155" />
      <circle cx="37" cy="28" r="2.5" fill="#334155" />
      <path d="M 24 36 Q 30 42 36 36" fill="none" stroke="#334155" stroke-width="2" stroke-linecap="round" />
      <!-- Body -->
      <path d="M 12 75 C 12 55, 48 55, 48 75 Z" fill="#38BDF8" stroke="#334155" stroke-width="2" />
      <text x="30" y="92" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">{clean_sp_a}</text>
    </g>

    <!-- Center Dialogue Symbol -->
    <g transform="translate(155, 60)">
      <circle cx="15" cy="15" r="14" fill="#14778B" opacity="0.1" />
      <path d="M 5 15 Q 15 5 25 15" fill="none" stroke="#14778B" stroke-width="2.5" stroke-linecap="round" />
      <circle cx="15" cy="15" r="3" fill="#14778B" />
      <path d="M 25 15 Q 15 25 5 15" fill="none" stroke="#14778B" stroke-width="2.5" stroke-linecap="round" />
    </g>

    <!-- Speaker B (Right) -->
    <g transform="translate(220, 40)">
      <!-- Head -->
      <circle cx="30" cy="30" r="22" fill="#FED7AA" stroke="#334155" stroke-width="2" />
      <circle cx="23" cy="28" r="2.5" fill="#334155" />
      <circle cx="37" cy="28" r="2.5" fill="#334155" />
      <path d="M 24 36 Q 30 42 36 36" fill="none" stroke="#334155" stroke-width="2" stroke-linecap="round" />
      <!-- Body -->
      <path d="M 12 75 C 12 55, 48 55, 48 75 Z" fill="#818CF8" stroke="#334155" stroke-width="2" />
      <text x="30" y="92" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">{clean_sp_b}</text>
    </g>

    <!-- Key Situation Items/Details -->
    <text x="170" y="152" font-family="-apple-system, sans-serif" font-size="10.5" font-weight="bold" fill="#64748B" text-anchor="middle">{clean_details}</text>
  </g>

  <!-- Bottom Tip -->
  <rect x="30" y="244" width="340" height="42" rx="8" fill="#F8FAFC" stroke="#CBD5E1" stroke-width="1" />
  <text x="45" y="269" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#14778B">POINT：</text>
  <text x="95" y="269" font-family="-apple-system, sans-serif" font-size="11" fill="#475569">誰が・何を・どのような順序で行うか聞き取りましょう</text>
</svg>'''
    return svg

def make_arrow_svg(title, situation, question_speaker="発話者（あなた）", listener="相手"):
    """
    問題3「発話表現」用 矢印図 (4:3 ratio: 400x300)
    赤い太い矢印（➡）が話者を指し示す、JLPT公式本番仕様
    """
    clean_title = html.escape(title)
    clean_sit = html.escape(situation)
    clean_sp = html.escape(question_speaker)
    clean_lis = html.escape(listener)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.1" />
    </filter>
  </defs>

  <!-- Background -->
  <rect width="400" height="300" rx="16" fill="#FDF4F5" stroke="#FBCFE8" stroke-width="1.5" />

  <!-- Header -->
  <rect x="20" y="16" width="110" height="24" rx="12" fill="#B8596E" />
  <text x="75" y="32" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">発話表現（場面）</text>
  <text x="140" y="33" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#881337">{clean_title}</text>

  <!-- Stage Box -->
  <rect x="25" y="52" width="350" height="185" rx="14" fill="#FFFFFF" stroke="#F43F5E" stroke-width="1.5" filter="url(#shadow)" />

  <!-- Target Speaker with BIG RED ARROW (Pointed by JLPT arrow) -->
  <g transform="translate(65, 80)">
    <!-- RED ARROW POINTING TO THIS PERSON -->
    <path d="M -25 25 L 5 25 L 5 15 L 25 30 L 5 45 L 5 35 L -25 35 Z" fill="#E11D48" stroke="#9F1239" stroke-width="1.5" />
    
    <!-- Character Head -->
    <circle cx="60" cy="30" r="24" fill="#FED7AA" stroke="#334155" stroke-width="2.5" />
    <circle cx="53" cy="27" r="2.5" fill="#334155" />
    <circle cx="67" cy="27" r="2.5" fill="#334155" />
    <path d="M 54 36 Q 60 42 66 36" fill="none" stroke="#334155" stroke-width="2" stroke-linecap="round" />
    <!-- Character Body -->
    <path d="M 40 85 C 40 60, 80 60, 80 85 Z" fill="#F43F5E" stroke="#334155" stroke-width="2.5" />
    <rect x="30" y="93" width="60" height="20" rx="6" fill="#FFE4E6" stroke="#E11D48" stroke-width="1" />
    <text x="60" y="107" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#9F1239" text-anchor="middle">{clean_sp}</text>
  </g>

  <!-- Speech bubble asking "何と言いますか？" -->
  <g transform="translate(160, 68)">
    <path d="M 10 25 Q 10 0 45 0 L 105 0 Q 140 0 140 25 L 140 45 Q 140 70 105 70 L 40 70 L 15 85 L 22 70 Q 10 70 10 45 Z" fill="#FFF1F2" stroke="#E11D48" stroke-width="1.5" />
    <text x="75" y="32" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#BE123C" text-anchor="middle">こんなとき、</text>
    <text x="75" y="52" font-family="-apple-system, sans-serif" font-size="13" font-weight="black" fill="#E11D48" text-anchor="middle">何と言いますか？</text>
  </g>

  <!-- Listener (Right) -->
  <g transform="translate(265, 80)">
    <!-- Head -->
    <circle cx="40" cy="30" r="22" fill="#E2E8F0" stroke="#475569" stroke-width="2" />
    <circle cx="33" cy="28" r="2.5" fill="#475569" />
    <circle cx="47" cy="28" r="2.5" fill="#475569" />
    <!-- Body -->
    <path d="M 22 85 C 22 62, 58 62, 58 85 Z" fill="#94A3B8" stroke="#475569" stroke-width="2" />
    <text x="40" y="107" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">{clean_lis}</text>
  </g>

  <!-- Bottom Situation Instruction -->
  <rect x="25" y="245" width="350" height="42" rx="8" fill="#FFF" stroke="#E2E8F0" stroke-width="1" />
  <text x="38" y="270" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#E11D48">場面：</text>
  <text x="75" y="270" font-family="-apple-system, sans-serif" font-size="11" fill="#334155">{clean_sit}</text>
</svg>'''
    return svg

def make_4grid_svg(title, item1, item2, item3, item4):
    """
    4分割選択肢イラスト (4:3 ratio: 400x300)
    """
    clean_title = html.escape(title)
    c1 = html.escape(item1)
    c2 = html.escape(item2)
    c3 = html.escape(item3)
    c4 = html.escape(item4)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 300" width="100%" height="100%">
  <!-- Background -->
  <rect width="400" height="300" rx="16" fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1.5" />

  <!-- Header -->
  <rect x="20" y="14" width="80" height="22" rx="11" fill="#14778B" />
  <text x="60" y="29" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">選択肢</text>
  <text x="110" y="30" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#1E293B">{clean_title}</text>

  <!-- 4 Grid Boxes -->
  <!-- Box 1 -->
  <g transform="translate(25, 48)">
    <rect width="165" height="110" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
    <circle cx="24" cy="24" r="12" fill="#14778B" />
    <text x="24" y="28" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
    <text x="82" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">{c1}</text>
  </g>

  <!-- Box 2 -->
  <g transform="translate(210, 48)">
    <rect width="165" height="110" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
    <circle cx="24" cy="24" r="12" fill="#14778B" />
    <text x="24" y="28" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">2</text>
    <text x="82" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">{c2}</text>
  </g>

  <!-- Box 3 -->
  <g transform="translate(25, 170)">
    <rect width="165" height="110" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
    <circle cx="24" cy="24" r="12" fill="#14778B" />
    <text x="24" y="28" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3</text>
    <text x="82" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">{c3}</text>
  </g>

  <!-- Box 4 -->
  <g transform="translate(210, 170)">
    <rect width="165" height="110" rx="10" fill="#FFFFFF" stroke="#CBD5E1" stroke-width="1.5" />
    <circle cx="24" cy="24" r="12" fill="#14778B" />
    <text x="24" y="28" font-family="-apple-system, sans-serif" font-size="11" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4</text>
    <text x="82" y="65" font-family="-apple-system, sans-serif" font-size="12" font-weight="bold" fill="#1E293B" text-anchor="middle">{c4}</text>
  </g>
</svg>'''
    return svg
