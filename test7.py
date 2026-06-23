# import sys
# import random
# import math  # <-- Added this (required for cos/sin in orbiting particles)

# from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, Property, QPointF, QRectF
# from PySide6.QtWidgets import (
#     QApplication, QDialog, QVBoxLayout, QTextBrowser, QLineEdit, QWidget, QLabel
# )
# from PySide6.QtGui import (
#     QPainter, QFont, QColor, QRadialGradient, QBrush, QPen, QLinearGradient, QFontMetrics
# )

# class FuturisticSplash(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.resize(900, 650)

#         # Internal state
#         self._logo_opacity = 0.0
#         self._logo_scale = 0.8
#         self._title_opacity = 0.0
#         self._tagline_opacity = 0.0
#         self._progress = 0
#         self._scan_line_y = -self.height()
#         self._glitch_offset = 0
#         self._typed_text = ""
#         self.full_title = "Optical Cabinet"
#         self.current_char = 0

#         # Particles
#         self.particles = []
#         for i in range(20):
#             angle = i * 18
#             self.particles.append({
#                 'angle': angle,
#                 'radius': 150 + random.randint(-50, 50),
#                 'speed': 1 + random.random() * 2,
#                 'size': 3 + random.randint(0, 4),
#                 'color': QColor(0, 255, 200, 150) if i % 2 == 0 else QColor(200, 0, 255, 150),
#                 'trail': []
#             })

#         self.bg_particles = []
#         for _ in range(50):
#             self.bg_particles.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'dx': (random.random() - 0.5) * 0.5,
#                 'dy': (random.random() - 0.5) * 0.5,
#                 'size': 1 + random.random() * 2,
#                 'opacity': 0.2 + random.random() * 0.3
#             })

#         self.startAnimations()

#     # Qt Properties
#     @Property(float)
#     def logo_opacity(self):
#         return self._logo_opacity

#     @logo_opacity.setter
#     def logo_opacity(self, value):
#         self._logo_opacity = value
#         self.update()

#     @Property(float)
#     def logo_scale(self):
#         return self._logo_scale

#     @logo_scale.setter
#     def logo_scale(self, value):
#         self._logo_scale = value
#         self.update()

#     @Property(float)
#     def title_opacity(self):
#         return self._title_opacity

#     @title_opacity.setter
#     def title_opacity(self, value):
#         self._title_opacity = value
#         self.update()

#     @Property(float)
#     def tagline_opacity(self):
#         return self._tagline_opacity

#     @tagline_opacity.setter
#     def tagline_opacity(self, value):
#         self._tagline_opacity = value
#         self.update()

#     def startAnimations(self):
#         # Fixed: added parent=self at the end
#         anim_opacity = QPropertyAnimation(self, b"logo_opacity", self)
#         anim_opacity.setDuration(1800)
#         anim_opacity.setStartValue(0.0)
#         anim_opacity.setEndValue(1.0)
#         anim_opacity.setEasingCurve(QEasingCurve.OutExpo)
#         anim_opacity.start()

#         anim_scale = QPropertyAnimation(self, b"logo_scale", self)
#         anim_scale.setDuration(2000)
#         anim_scale.setStartValue(0.8)
#         anim_scale.setEndValue(1.2)
#         anim_scale.setEasingCurve(QEasingCurve.OutBounce)
#         anim_scale.start()

#         # Title typing
#         self.title_timer = QTimer(self)
#         self.title_timer.timeout.connect(self.typeTitle)
#         self.title_timer.start(120)

#         # Tagline fade
#         QTimer.singleShot(3000, self.fadeInTagline)

#         # Main update loop
#         self.update_timer = QTimer(self)
#         self.update_timer.timeout.connect(self.updateElements)
#         self.update_timer.start(30)

#         # Finish splash
#         QTimer.singleShot(6000, self.finishSplash)

#     def typeTitle(self):
#         if self.current_char < len(self.full_title):
#             self.current_char += 1
#             self._typed_text = self.full_title[:self.current_char]
#             self.title_opacity = 1.0
#             self._glitch_offset = random.randint(-8, 8)
#             self.update()

#     def fadeInTagline(self):
#         anim = QPropertyAnimation(self, b"tagline_opacity", self)
#         anim.setDuration(1500)
#         anim.setStartValue(0.0)
#         anim.setEndValue(1.0)
#         anim.start()

#     def updateElements(self):
#         if self._progress < 100:
#             self._progress += 1

#         self._scan_line_y += 6
#         if self._scan_line_y > self.height():
#             self._scan_line_y = -50

#         for p in self.particles:
#             p['angle'] += p['speed']
#             if p['angle'] >= 360:
#                 p['angle'] -= 360
#             p['trail'].append((p['angle'], p['radius']))
#             if len(p['trail']) > 12:
#                 p['trail'].pop(0)

#         for bp in self.bg_particles:
#             bp['x'] += bp['dx']
#             bp['y'] += bp['dy']
#             if bp['x'] < 0 or bp['x'] > self.width():
#                 bp['dx'] *= -1
#             if bp['y'] < 0 or bp['y'] > self.height():
#                 bp['dy'] *= -1

#         if random.random() < 0.05:
#             self._glitch_offset = random.randint(-12, 12)
#         else:
#             self._glitch_offset *= 0.8

#         self.update()

#     def finishSplash(self):
#         self.update_timer.stop()
#         if self.title_timer.isActive():
#             self.title_timer.stop()

#         fade = QPropertyAnimation(self, b"windowOpacity", self)
#         fade.setDuration(1000)
#         fade.setStartValue(1.0)
#         fade.setEndValue(0.0)
#         fade.setEasingCurve(QEasingCurve.OutCirc)
#         fade.finished.connect(self.closeSplash)
#         fade.start()

#     def closeSplash(self):
#         self.close()
#         showMainWindow()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         painter.setRenderHint(QPainter.SmoothPixmapTransform)

#         # Background gradient
#         gradient = QLinearGradient(0, 0, 0, self.height())
#         gradient.setColorAt(0, QColor("#000015"))
#         gradient.setColorAt(1, QColor("#1a0033"))
#         painter.fillRect(self.rect(), QBrush(gradient))

#         # Grid
#         painter.setPen(QPen(QColor(0, 255, 255, 30), 1, Qt.DashLine))
#         for x in range(0, self.width(), 50):
#             painter.drawLine(x, 0, x, self.height())
#         for y in range(0, self.height(), 50):
#             painter.drawLine(0, y, self.width(), y)

#         # Background particles
#         for bp in self.bg_particles:
#             painter.setOpacity(bp['opacity'])
#             painter.setBrush(QColor(255, 255, 255))
#             painter.setPen(Qt.NoPen)
#             painter.drawEllipse(QPointF(bp['x'], bp['y']), bp['size'], bp['size'])
#         painter.setOpacity(1.0)

#         center_x = self.width() // 2
#         center_y = self.height() // 2 - 100

#         # Logo
#         painter.save()
#         painter.translate(center_x, center_y)
#         painter.scale(self._logo_scale, self._logo_scale)
#         painter.setOpacity(self._logo_opacity)

#         glow = QRadialGradient(0, 0, 150)
#         glow.setColorAt(0, QColor(0, 255, 200, 100))
#         glow.setColorAt(1, QColor(0, 255, 200, 0))
#         painter.setBrush(QBrush(glow))
#         painter.drawEllipse(-150, -150, 300, 300)

#         pen = QPen(QColor("#00ffcc"), 12, Qt.SolidLine, Qt.RoundCap)
#         painter.setPen(pen)
#         painter.setBrush(Qt.NoBrush)
#         painter.drawEllipse(-120, -60, 120, 120)
#         painter.drawEllipse(0, -60, 120, 120)
#         painter.drawLine(-60, -30, 0, -30)

#         painter.setBrush(QColor(200, 0, 255, 120))
#         painter.drawEllipse(-90, -30, 40, 40)
#         painter.drawEllipse(30, -30, 40, 40)

#         painter.restore()

#         # Orbiting particles (trails + main)
#         for p in self.particles:
#             # Trails
#             for i, (a, r) in enumerate(p['trail']):
#                 op = (i + 1) / len(p['trail']) * 0.6
#                 painter.setOpacity(op * 0.7)
#                 rad = a * math.pi / 180
#                 x = center_x + r * math.cos(rad)
#                 y = center_y + r * math.sin(rad)
#                 painter.setBrush(p['color'])
#                 painter.drawEllipse(QPointF(x, y), p['size'] / 2, p['size'] / 2)

#             # Main particle
#             rad = p['angle'] * math.pi / 180
#             x = center_x + p['radius'] * math.cos(rad)
#             y = center_y + p['radius'] * math.sin(rad)
#             painter.setOpacity(1.0)
#             painter.setBrush(p['color'])
#             painter.drawEllipse(QPointF(x, y), p['size'], p['size'])

#         # Title with glitch
#         painter.setOpacity(self._title_opacity)
#         title_font = QFont("Courier New", 52, QFont.Bold)
#         painter.setFont(title_font)
#         metrics = QFontMetrics(title_font)
#         w = metrics.horizontalAdvance(self._typed_text)

#         painter.setPen(QColor("#00ffcc"))
#         painter.drawText(center_x - w//2 + self._glitch_offset, center_y + 100, self._typed_text)

#         painter.setPen(QColor(255, 0, 150, 180))
#         painter.drawText(center_x - w//2 + self._glitch_offset + 5, center_y + 100, self._typed_text)
#         painter.setPen(QColor(0, 200, 255, 180))
#         painter.drawText(center_x - w//2 + self._glitch_offset - 5, center_y + 100, self._typed_text)

#         # Tagline
#         painter.setOpacity(self._tagline_opacity)
#         painter.setFont(QFont("Courier New", 20))
#         painter.setPen(QColor("#99ccff"))
#         painter.drawText(QRectF(0, center_y + 180, self.width(), 50), Qt.AlignCenter, "Next-Gen Optical Management System")

#         # Scan line
#         scan_grad = QLinearGradient(0, self._scan_line_y, 0, self._scan_line_y + 60)
#         scan_grad.setColorAt(0, QColor(0, 255, 200, 0))
#         scan_grad.setColorAt(0.5, QColor(0, 255, 200, 120))
#         scan_grad.setColorAt(1, QColor(0, 255, 200, 0))
#         painter.setBrush(QBrush(scan_grad))
#         painter.drawRect(0, int(self._scan_line_y), self.width(), 60)

#         # Percentage counter
#         percent_text = f"{self._progress}%"
#         painter.setFont(QFont("Courier New", 80, QFont.Bold))
#         metrics = QFontMetrics(painter.font())
#         pw = metrics.horizontalAdvance(percent_text)

#         glow = QRadialGradient(center_x, self.height() - 100, 200)
#         glow.setColorAt(0, QColor(0, 255, 200, 160))
#         glow.setColorAt(1, QColor(0, 255, 200, 0))
#         painter.setBrush(QBrush(glow))
#         painter.drawEllipse(center_x - 200, self.height() - 180, 400, 120)

#         painter.setPen(QColor("#00ffcc"))
#         painter.drawText(center_x - pw//2, self.height() - 80, percent_text)


# class MainWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Optical Cabinet")
#         self.resize(1000, 700)
#         self.setStyleSheet("background:#0f172a; color:#e2e8f0; font-family: 'Segoe UI';")

#         layout = QVBoxLayout()
#         label = QLabel("Welcome to the Future of Optical Management!")
#         label.setAlignment(Qt.AlignCenter)
#         label.setFont(QFont("Courier New", 28))
#         label.setStyleSheet("color: #00ffcc;")
#         layout.addWidget(label)

#         self.browser = QTextBrowser()
#         self.line_edit = QLineEdit("Enter command...")
#         self.line_edit.setStyleSheet("padding: 10px; font-size: 16px;")
#         layout.addWidget(self.browser)
#         layout.addWidget(self.line_edit)
#         self.setLayout(layout)

#         self.line_edit.returnPressed.connect(self.on_enter)

#     def on_enter(self):
#         text = self.line_edit.text()
#         self.browser.append(f"> {text}")
#         self.line_edit.clear()


# def showMainWindow():
#     global main_win
#     main_win = MainWindow()
#     main_win.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     splash = FuturisticSplash()
#     splash.show()
#     app.processEvents()
#     sys.exit(app.exec())
# import sys
# import random
# import math

# from PySide6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, Property
# from PySide6.QtWidgets import (
#     QApplication, QDialog, QVBoxLayout, QTextBrowser, QLineEdit, QWidget, QLabel
# )
# # from PySide6.QtGui import (
# #     QPainter, QFont, QColor, QRadialGradient, QBrush, QPen, QLinearGradient, QFontMetrics, QPointF, QRectF
# # )
# from PySide6.QtGui import (
#     QPainter, QFont, QColor, QRadialGradient, QBrush, QPen, QLinearGradient, QFontMetrics
# )
# from PySide6.QtCore import QPointF, QRectF


# class SmoothSplash(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#         self.resize(900, 650)

#         # State
#         self._logo_opacity = 0.0
#         self._logo_scale = 0.8
#         self._title_opacity = 0.0
#         self._tagline_opacity = 0.0
#         self._progress = 0
#         self._wave_offset = 0
#         self._typed_text = ""
#         self.full_title = "Optical Cabinet"
#         self.current_char = 0

#         # Soft floating particles
#         self.particles = []
#         for i in range(25):
#             self.particles.append({
#                 'x': random.randint(0, self.width()),
#                 'y': random.randint(0, self.height()),
#                 'dx': (random.random() - 0.5) * 0.8,
#                 'dy': (random.random() - 0.5) * 0.8,
#                 'size': 4 + random.random() * 8,
#                 'opacity': 0.3 + random.random() * 0.4,
#                 'color': QColor(147, 197, 253, 100) if i % 2 == 0 else QColor(196, 181, 253, 100)
#             })

#         self.startAnimations()

#     # Properties
#     @Property(float)
#     def logo_opacity(self):
#         return self._logo_opacity
#     @logo_opacity.setter
#     def logo_opacity(self, value):
#         self._logo_opacity = value
#         self.update()

#     @Property(float)
#     def logo_scale(self):
#         return self._logo_scale
#     @logo_scale.setter
#     def logo_scale(self, value):
#         self._logo_scale = value
#         self.update()

#     @Property(float)
#     def title_opacity(self):
#         return self._title_opacity
#     @title_opacity.setter
#     def title_opacity(self, value):
#         self._title_opacity = value
#         self.update()

#     @Property(float)
#     def tagline_opacity(self):
#         return self._tagline_opacity
#     @tagline_opacity.setter
#     def tagline_opacity(self, value):
#         self._tagline_opacity = value
#         self.update()

#     def startAnimations(self):
#         # Logo opacity - fixed by assigning to variable first
#         logo_opacity_anim = QPropertyAnimation(self, b"logo_opacity", self)
#         logo_opacity_anim.setDuration(2000)
#         logo_opacity_anim.setStartValue(0.0)
#         logo_opacity_anim.setEndValue(1.0)
#         logo_opacity_anim.setEasingCurve(QEasingCurve.OutCubic)
#         logo_opacity_anim.start()

#         # Logo scale
#         logo_scale_anim = QPropertyAnimation(self, b"logo_scale", self)
#         logo_scale_anim.setDuration(2500)
#         logo_scale_anim.setStartValue(0.8)
#         logo_scale_anim.setEndValue(1.1)
#         logo_scale_anim.setEasingCurve(QEasingCurve.OutElastic)
#         logo_scale_anim.start()

#         # Title typing
#         self.title_timer = QTimer(self)
#         self.title_timer.timeout.connect(self.typeTitle)
#         self.title_timer.start(100)

#         # Tagline fade
#         QTimer.singleShot(2800, self.fadeInTagline)

#         # Main update loop
#         self.update_timer = QTimer(self)
#         self.update_timer.timeout.connect(self.updateElements)
#         self.update_timer.start(30)

#         # Finish after ~6 seconds
#         QTimer.singleShot(6000, self.finishSplash)

#     def typeTitle(self):
#         if self.current_char < len(self.full_title):
#             self.current_char += 1
#             self._typed_text = self.full_title[:self.current_char]
#             self.title_opacity = 1.0
#             self.update()

#     def fadeInTagline(self):
#         tagline_anim = QPropertyAnimation(self, b"tagline_opacity", self)
#         tagline_anim.setDuration(1800)
#         tagline_anim.setStartValue(0.0)
#         tagline_anim.setEndValue(1.0)
#         tagline_anim.start()

#     def updateElements(self):
#         if self._progress < 100:
#             self._progress += 1

#         self._wave_offset += 0.5

#         for p in self.particles:
#             p['x'] += p['dx']
#             p['y'] += p['dy']
#             if p['x'] < -50 or p['x'] > self.width() + 50:
#                 p['dx'] *= -1
#             if p['y'] < -50 or p['y'] > self.height() + 50:
#                 p['dy'] *= -1

#         self.update()

#     def finishSplash(self):
#         self.update_timer.stop()
#         if self.title_timer.isActive():
#             self.title_timer.stop()

#         fade_anim = QPropertyAnimation(self, b"windowOpacity", self)
#         fade_anim.setDuration(1200)
#         fade_anim.setStartValue(1.0)
#         fade_anim.setEndValue(0.0)
#         fade_anim.setEasingCurve(QEasingCurve.OutQuart)
#         fade_anim.finished.connect(self.closeSplash)
#         fade_anim.start()

#     def closeSplash(self):
#         self.close()
#         showMainWindow()

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.setRenderHint(QPainter.Antialiasing)
#         painter.setRenderHint(QPainter.SmoothPixmapTransform)

#         # Soft gradient background
#         gradient = QLinearGradient(0, 0, self.width(), self.height())
#         gradient.setColorAt(0, QColor("#0f172a"))
#         gradient.setColorAt(0.5, QColor("#1e293b"))
#         gradient.setColorAt(1, QColor("#312e81"))
#         painter.fillRect(self.rect(), QBrush(gradient))

#         # Floating soft particles
#         for p in self.particles:
#             painter.setOpacity(p['opacity'])
#             glow = QRadialGradient(p['x'], p['y'], p['size'] * 3)
#             glow.setColorAt(0, p['color'])
#             glow.setColorAt(1, QColor(0, 0, 0, 0))
#             painter.setBrush(QBrush(glow))
#             painter.setPen(Qt.NoPen)
#             painter.drawEllipse(QPointF(p['x'], p['y']), p['size'], p['size'])
#         painter.setOpacity(1.0)

#         center_x = self.width() // 2
#         center_y = self.height() // 2 - 80

#         # Logo with soft glow
#         painter.save()
#         painter.translate(center_x, center_y)
#         painter.scale(self._logo_scale, self._logo_scale)
#         painter.setOpacity(self._logo_opacity)

#         glow = QRadialGradient(0, 0, 180)
#         glow.setColorAt(0, QColor(147, 197, 253, 80))
#         glow.setColorAt(1, QColor(147, 197, 253, 0))
#         painter.setBrush(QBrush(glow))
#         painter.drawEllipse(-180, -180, 360, 360)

#         pen = QPen(QColor("#06b6d4"), 10, Qt.SolidLine, Qt.RoundCap)
#         painter.setPen(pen)
#         painter.setBrush(Qt.NoBrush)
#         painter.drawEllipse(-120, -60, 120, 120)
#         painter.drawEllipse(0, -60, 120, 120)
#         painter.drawLine(-60, -30, 0, -30)

#         painter.setBrush(QColor(255, 255, 255, 60))
#         painter.drawEllipse(-90, -40, 50, 50)
#         painter.drawEllipse(30, -40, 50, 50)

#         painter.restore()

#         # Title
#         painter.setOpacity(self._title_opacity)
#         title_font = QFont("Segoe UI", 56, QFont.Bold)
#         painter.setFont(title_font)
#         painter.setPen(QColor("#e0e7ff"))
#         metrics = QFontMetrics(title_font)
#         w = metrics.horizontalAdvance(self._typed_text)
#         painter.drawText(center_x - w//2, center_y + 120, self._typed_text)

#         # Tagline
#         painter.setOpacity(self._tagline_opacity)
#         painter.setFont(QFont("Segoe UI", 22))
#         painter.setPen(QColor("#a5b4fc"))
#         painter.drawText(QRectF(0, center_y + 180, self.width(), 60), Qt.AlignCenter, "Premium Optical Management System")

#         # Smooth wave texture
#         wave_y = self.height() - 150
#         painter.setPen(Qt.NoPen)
#         for i in range(-100, self.width() + 100, 20):
#             x = i
#             y = wave_y + math.sin((x + self._wave_offset) * 0.02) * 30
#             wave_glow = QRadialGradient(x, y, 60)
#             wave_glow.setColorAt(0, QColor(147, 197, 253, 80))
#             wave_glow.setColorAt(1, QColor(147, 197, 253, 0))
#             painter.setBrush(QBrush(wave_glow))
#             painter.drawEllipse(x - 30, y - 30, 60, 60)

#         # Percentage counter
#         percent_text = f"{self._progress}%"
#         painter.setFont(QFont("Segoe UI", 84, QFont.Bold))
#         metrics = QFontMetrics(painter.font())
#         pw = metrics.horizontalAdvance(percent_text)

#         glow = QRadialGradient(center_x, self.height() - 100, 220)
#         glow.setColorAt(0, QColor(6, 182, 212, 180))
#         glow.setColorAt(1, QColor(6, 182, 212, 0))
#         painter.setBrush(QBrush(glow))
#         painter.drawEllipse(center_x - 220, self.height() - 180, 440, 140)

#         painter.setPen(QColor("#06b6d4"))
#         painter.drawText(center_x - pw//2, self.height() - 70, percent_text)


# class MainWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Optical Cabinet")
#         self.resize(1000, 700)
#         self.setStyleSheet("background:#f1f5f9; color:#1e293b;")

#         layout = QVBoxLayout()
#         label = QLabel("Welcome to Optical Cabinet")
#         label.setAlignment(Qt.AlignCenter)
#         label.setFont(QFont("Segoe UI", 32))
#         label.setStyleSheet("color: #4f46e5; padding: 40px;")
#         layout.addWidget(label)

#         self.browser = QTextBrowser()
#         self.line_edit = QLineEdit("Type here...")
#         layout.addWidget(self.browser)
#         layout.addWidget(self.line_edit)
#         self.setLayout(layout)

#         self.line_edit.returnPressed.connect(self.on_enter)

#     def on_enter(self):
#         text = self.line_edit.text()
#         self.browser.append(f"You: {text}")
#         self.line_edit.clear()


# def showMainWindow():
#     global main_win
#     main_win = MainWindow()
#     main_win.show()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     splash = SmoothSplash()
#     splash.show()
#     app.processEvents()
#     sys.exit(app.exec())


# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# splash_screen.py
# import sys
# from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QTimer
# from PySide6.QtGui import QColor, QPixmap
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QGraphicsDropShadowEffect, QGraphicsOpacityEffect
# )

# # Load your generated UI class
# # from your_ui_file import Ui_MainWindow  # Replace with actual filename, e.g. splash_screenbaWtjV.py
# from ui_ux.splash_screen.ui_splash_screen2 import Ui_MainWindow  
# class SplashScreen(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         # Set frameless + translucent for futuristic feel
#         self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)

#         # Dark space background
#         self.ui.centralwidget.setStyleSheet("background-color: #0a0e1a;")

#         # === Enhanced Main Frame ===
#         self.ui.main_frame.setStyleSheet("""
#             background: qlineargradient(spread:pad, x1:0, y1:0.2, x2:1, y2:0.6,
#                                         stop:0 #0158b8, stop:1 #1e2270);
#             border-radius: 25px;
#             border: 3px solid rgba(0, 220, 255, 120);
#         """)

#         glow_main = QGraphicsDropShadowEffect(self.ui.main_frame)
#         glow_main.setBlurRadius(50)
#         glow_main.setColor(QColor(0, 255, 255, 160))
#         glow_main.setOffset(0, 0)
#         self.ui.main_frame.setGraphicsEffect(glow_main)

#         # === Middle Circle Frame - Futuristic Spinning Neon Ring ===
#         self.ui.middle_cricle_frame.setStyleSheet("""
#             background: transparent;
#             border: 12px solid transparent;
#             border-top: 12px solid #00ffff;
#             border-radius: 200px;
#         """)

#         ring_glow = QGraphicsDropShadowEffect(self.ui.middle_cricle_frame)
#         ring_glow.setBlurRadius(60)
#         ring_glow.setColor(QColor(0, 255, 255, 220))
#         ring_glow.setOffset(0, 0)
#         self.ui.middle_cricle_frame.setGraphicsEffect(ring_glow)

#         # Spinning animation
#         self.angle = 0
#         self.spin_timer = QTimer(self)
#         self.spin_timer.timeout.connect(self.spin_ring)
#         self.spin_timer.start(40)

#         # === Shoe Logo Area ===
#         self.ui.shoes_border_frame.setStyleSheet("""
#             background: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0,
#                                         stop:0 rgba(30, 40, 100, 200), stop:1 rgba(0, 100, 200, 80));
#             border: 7px solid rgba(0, 220, 255, 200);
#             border-radius: 25px;
#         """)

#         shoe_glow = QGraphicsDropShadowEffect(self.ui.shoes_border_frame)
#         shoe_glow.setBlurRadius(45)
#         shoe_glow.setColor(QColor(0, 255, 255, 180))
#         shoe_glow.setOffset(0, 0)
#         self.ui.shoes_border_frame.setGraphicsEffect(shoe_glow)

#         # Shoe image (ensure it scales nicely)
#         self.ui.shoe_frame.setStyleSheet("""
#             image: url(:/logo/logo1.png);
#             background: transparent;
#             border: none;
#         """)

#         # === Bottom Info Panel ===
#         self.ui.more_info_frame.setStyleSheet("""
#             background: rgba(20, 30, 80, 240);
#             border-radius: 25px;
#             border: 4px solid rgba(0, 200, 255, 140);
#         """)

#         info_glow = QGraphicsDropShadowEffect(self.ui.more_info_frame)
#         info_glow.setBlurRadius(40)
#         info_glow.setColor(QColor(0, 180, 255, 120))
#         info_glow.setOffset(0, 0)
#         self.ui.more_info_frame.setGraphicsEffect(info_glow)

#         # Update text colors for futuristic look
#         self.ui.loading_status.setStyleSheet("""
#             color: #00ffff;
#             background: transparent;
#             text-shadow: 0 0 10px #00ffff;
#         """)

#         self.ui.loading_progress.setStyleSheet("color: #a0ffff; background: transparent;")
#         self.ui.app_info.setStyleSheet("color: #88ccff; background: transparent;")

#         # === WELCOME Label - Enhanced with Fade-in & Glow ===
#         self.ui.welcome_label.setStyleSheet("""
#             color: #00ffff;
#             background: transparent;
#             border: none;
#         """)

#         welcome_glow = QGraphicsDropShadowEffect(self.ui.welcome_label)
#         welcome_glow.setBlurRadius(50)
#         welcome_glow.setColor(QColor(0, 255, 255, 255))
#         welcome_glow.setOffset(0, 0)

#         # Fade-in effect
#         opacity = QGraphicsOpacityEffect(self.ui.welcome_label)
#         self.ui.welcome_label.setGraphicsEffect(opacity)

#         self.fade_anim = QPropertyAnimation(opacity, b"opacity")
#         self.fade_anim.setDuration(3000)
#         self.fade_anim.setStartValue(0.0)
#         self.fade_anim.setEndValue(1.0)
#         self.fade_anim.setEasingCurve(QEasingCurve.OutCubic)
#         self.fade_anim.start()

#         # Apply glow after fade (combine effects)
#         self.ui.welcome_label.setGraphicsEffect(welcome_glow)

#         # === Pulsing Glow Animation ===
#         self.pulse_timer = QTimer(self)
#         self.pulse_timer.timeout.connect(self.pulse_glow)
#         self.pulse_timer.start(1200)

#     def spin_ring(self):
#         colors = ["#00ffff", "#00ddff", "#00bbff", "#0099ff"]
#         color = colors[self.angle % len(colors)]
#         self.ui.middle_cricle_frame.setStyleSheet(f"""
#             background: transparent;
#             border: 12px solid transparent;
#             border-top: 12px solid {color};
#             border-radius: 200px;
#         """)
#         self.angle += 1

#     def pulse_glow(self):
#         effects = [
#             self.ui.main_frame.graphicsEffect(),
#             self.ui.shoes_border_frame.graphicsEffect(),
#             self.ui.middle_cricle_frame.graphicsEffect()
#         ]
#         for effect in effects:
#             if isinstance(effect, QGraphicsDropShadowEffect):
#                 alpha = 220 if effect.color().alpha() > 180 else 140
#                 effect.setColor(QColor(0, 255, 255, alpha))


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     splash = SplashScreen()
#     splash.show()

#     # Simulate loading - replace with your actual main window launch
#     QTimer.singleShot(8000, splash.close)

#     sys.exit(app.exec())


import sys
import time
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget,
    QLabel, QLineEdit, QTextEdit, QDateTimeEdit, QCheckBox,
    QPushButton, QTableWidget, QHeaderView, QAbstractItemView,
    QGraphicsOpacityEffect, QGraphicsDropShadowEffect
)
from PySide6.QtCore import (
    QDateTime, QPropertyAnimation, QEasingCurve, Qt,
    QTimer, QRect, QPoint
)
from PySide6.QtGui import QColor, QLinearGradient, QBrush, QPalette

# ─── Futuristic Neon-Cyber Palette ────────────────────────────────
COLORS = {
    "bg_dark":      "#0a0e17",
    "bg":           "#0f1622",
    "surface":      "#121a2b",
    "surface_light":"#1a2540",
    "primary":      "#00d4ff",      # cyan
    "primary_dark": "#0099cc",
    "accent":       "#c300ff",      # neon magenta/purple
    "accent_dark":  "#8a00b3",
    "text":         "#e0f7ff",
    "text_soft":    "#88ccff",
    "border":       "#00aaff44",
    "glow":         "#00eaff66",
    "glow_purple":  "#c300ff44",
    "shadow":       "rgba(0, 212, 255, 0.18)",
}

class WhatsAppScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neo-WhatsApp Scheduler • 未来")
        self.resize(940, 680)
        
        self._apply_futuristic_style()
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(16, 16, 16, 16)
        main_layout.setSpacing(12)

        # ─── Tabs ───────────────────────────────────────
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        main_layout.addWidget(self.tabs)

        self._create_scheduler_tab()
        self._create_contacts_tab()
        self._create_patients_tab()

        # Animations on load
        self.animate_window_open()
        QTimer.singleShot(400, lambda: self.animate_tab_switch(0))

        # Connect tab change with animation
        self.tabs.currentChanged.connect(self.animate_tab_switch)

    def _apply_futuristic_style(self):
        p = COLORS
        style = f"""
        QWidget {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {p['bg_dark']}, stop:1 {p['bg']});
            color: {p['text']};
            font-family: "Segoe UI", "Orbitron", "Fira Code", monospace;
            font-size: 14px;
        }}

        QTabWidget::pane {{
            border: 1px solid {p['border']};
            background: {p['surface']};
            border-radius: 12px;
            box-shadow: 0 0 25px {p['glow']};
        }}

        QTabBar::tab {{
            background: transparent;
            color: {p['text_soft']};
            padding: 14px 32px;
            margin: 0 4px -2px 0;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
            border: 1px solid transparent;
        }}

        QTabBar::tab:selected {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {p['primary']}33, stop:1 transparent);
            color: {p['primary']};
            border: 1px solid {p['primary']}88;
            border-bottom: 2px solid {p['primary']};
            font-weight: bold;
        }}

        QTabBar::tab:hover {{
            color: white;
            background: {p['glow']}22;
        }}

        QLineEdit, QTextEdit, QDateTimeEdit {{
            background: {p['surface_light']};
            border: 1px solid {p['border']};
            border-radius: 8px;
            padding: 10px 14px;
            color: {p['text']};
        }}

        QLineEdit:focus, QTextEdit:focus, QDateTimeEdit:focus {{
            border: 2px solid {p['primary']};
            background: {p['surface']};
            box-shadow: 0 0 18px {p['glow']}, inset 0 0 8px {p['glow']};
        }}

        QPushButton {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {p['primary']}, stop:1 {p['primary_dark']});
            color: black;
            border: none;
            border-radius: 10px;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 14px;
        }}

        QPushButton:hover {{
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 {p['primary']}, stop:1 {p['accent']});
            box-shadow: 0 0 20px {p['glow']}, 0 0 40px {p['glow_purple']};
        }}

        QPushButton:pressed {{
            background: {p['accent_dark']};
        }}

        QTableWidget {{
            background: {p['surface']};
            color: {p['text']};
            gridline-color: {p['border']};
            selection-background-color: {p['primary']}88;
            selection-color: black;
            alternate-background-color: {p['surface_light']};
        }}

        QHeaderView::section {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {p['primary']}, stop:1 {p['primary_dark']});
            color: black;
            padding: 10px;
            border: none;
        }}

        QCheckBox::indicator {{
            width: 20px;
            height: 20px;
            border: 2px solid {p['primary']};
            border-radius: 5px;
            background: {p['surface_light']};
        }}

        QCheckBox::indicator:checked {{
            background: qlineargradient(x1:0,y1:0,x2:1,y2:1,
                stop:0 {p['primary']}, stop:1 {p['accent']});
            image: none;
        }}
        """
        self.setStyleSheet(style)

    def _create_scheduler_tab(self):
        tab = QWidget()
        lay = QVBoxLayout(tab)
        lay.setSpacing(14)

        lay.addWidget(QLabel("Target Chat / Number"))
        self.chat_input = QLineEdit()
        lay.addWidget(self.chat_input)

        lay.addWidget(QLabel("Message Payload"))
        self.message_input = QTextEdit()
        self.message_input.setMinimumHeight(120)
        lay.addWidget(self.message_input)

        lay.addWidget(QLabel("Execution Timestamp"))
        self.datetime_input = QDateTimeEdit(QDateTime.currentDateTime())
        self.datetime_input.setCalendarPopup(True)
        lay.addWidget(self.datetime_input)

        self.persistent_check = QCheckBox("Persistent Quantum Session")
        lay.addWidget(self.persistent_check)

        self.add_btn = QPushButton("SCHEDULE TRANSMISSION ➜")
        self.add_btn.clicked.connect(self.animate_schedule_click)
        lay.addWidget(self.add_btn)

        self.jobs_table = QTableWidget(0, 4)
        self.jobs_table.setHorizontalHeaderLabels(["Target", "Payload", "When", "Status"])
        self.jobs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        lay.addWidget(self.jobs_table)

        self.tabs.addTab(tab, "Scheduler Core")

    def _create_contacts_tab(self):
        tab = QWidget()
        lay = QVBoxLayout(tab)

        search_lay = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search neural contacts…")
        search_btn = QPushButton("SCAN")
        search_lay.addWidget(self.search_input)
        search_lay.addWidget(search_btn)
        lay.addLayout(search_lay)

        self.contacts_table = QTableWidget(0, 4)
        self.contacts_table.setHorizontalHeaderLabels(["Alias", "Node", "Division", "Tag"])
        lay.addWidget(self.contacts_table)

        btn_row = QHBoxLayout()
        for txt, slot in [
            ("ADD NODE", self.dummy),
            ("MODIFY", self.dummy),
            ("TERMINATE", self.dummy),
            ("TRANSMIT TO SELECTED", self.dummy)
        ]:
            b = QPushButton(txt)
            b.clicked.connect(slot)
            btn_row.addWidget(b)
            self.animate_hover_glow_scale(b)
        lay.addLayout(btn_row)

        self.tabs.addTab(tab, "Neural Contacts")

    def _create_patients_tab(self):
        tab = QWidget()
        lay = QVBoxLayout(tab)
        self.tableWidget = QTableWidget(0, 8)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Subject", "EML", "LINK", "LOC", "Role", "Cycle", "Type"
        ])
        lay.addWidget(self.tableWidget)

        btn_row = QHBoxLayout()
        refresh = QPushButton("SYNC DATABASE")
        use_sel = QPushButton("TRANSMIT SELECTED SUBJECTS")
        for b in [refresh, use_sel]:
            btn_row.addWidget(b)
            self.animate_hover_glow_scale(b)
        lay.addLayout(btn_row)

        self.tabs.addTab(tab, "Subject Registry")

    # ─── Animations ──────────────────────────────────────────────────────

    def animate_window_open(self):
        self.setWindowOpacity(0.0)
        anim = QPropertyAnimation(self, b"windowOpacity")
        anim.setDuration(900)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.Type.OutExpo)
        anim.start()

    def animate_tab_switch(self, index):
        widget = self.tabs.widget(index)
        if not widget:
            return

        effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(effect)

        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(550)
        anim.setStartValue(0.3)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        anim.start()

    def animate_hover_glow_scale(self, widget):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(18)
        shadow.setColor(QColor(COLORS["glow"]))
        shadow.setOffset(0, 0)
        widget.setGraphicsEffect(shadow)

        def enter(e):
            anim_scale = QPropertyAnimation(widget, b"geometry")
            anim_scale.setDuration(220)
            r = widget.geometry()
            anim_scale.setStartValue(r)
            anim_scale.setEndValue(r.adjusted(-4,-4,4,4))
            anim_scale.setEasingCurve(QEasingCurve.Type.OutBack)

            anim_glow = QPropertyAnimation(shadow, b"blurRadius")
            anim_glow.setDuration(220)
            anim_glow.setStartValue(18)
            anim_glow.setEndValue(32)

            anim_scale.start()
            anim_glow.start()

        def leave(e):
            anim_scale = QPropertyAnimation(widget, b"geometry")
            anim_scale.setDuration(280)
            r = widget.geometry()
            anim_scale.setStartValue(r)
            anim_scale.setEndValue(r.adjusted(4,4,-4,-4))
            anim_scale.setEasingCurve(QEasingCurve.Type.OutCubic)

            anim_glow = QPropertyAnimation(shadow, b"blurRadius")
            anim_glow.setDuration(280)
            anim_glow.setStartValue(32)
            anim_glow.setEndValue(18)

            anim_scale.start()
            anim_glow.start()

        widget.enterEvent = enter
        widget.leaveEvent = leave
        widget.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

    def animate_schedule_click(self):
        # Button pulse + fake "transmitting" animation
        self.add_btn.setEnabled(False)
        self.add_btn.setText("TRANSMITTING...")

        pulse = QPropertyAnimation(self.add_btn, b"geometry")
        pulse.setDuration(180)
        r = self.add_btn.geometry()
        pulse.setStartValue(r)
        pulse.setEndValue(r.adjusted(-6,-6,6,6))
        pulse.setEasingCurve(QEasingCurve.Type.OutBack)

        back = QPropertyAnimation(self.add_btn, b"geometry")
        back.setDuration(400)
        back.setStartValue(r.adjusted(-6,-6,6,6))
        back.setEndValue(r)
        back.setEasingCurve(QEasingCurve.Type.OutElastic)

        def finish():
            self.add_btn.setText("SCHEDULE TRANSMISSION ➜")
            self.add_btn.setEnabled(True)

        pulse.finished.connect(back.start)
        back.finished.connect(finish)

        pulse.start()

    def dummy(self):
        pass  # placeholder

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Optional: global dark/futuristic palette tweak
    palette = app.palette()
    palette.setColor(QPalette.ColorRole.Window, QColor(COLORS["bg"]))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(COLORS["text"]))
    app.setPalette(palette)

    window = WhatsAppScheduler()
    window.show()
    sys.exit(app.exec())