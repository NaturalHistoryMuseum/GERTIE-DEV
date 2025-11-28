# Changelog

All notable changes to the GERTIE project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Strategic Planning
- Comprehensive Qt migration analysis completed (2025-11-10)
- Strategic plan created: Qt migration over Tkinter optimization
- 8-phase implementation roadmap established (Dec 2025 - Mar 2026)
- Target: April 2026 DiSSCo UK launch (90+ institutions)

### Planned - Phase 0 (Week of 2025-11-10)
- Telemetry system deployment to all 8 cameras
- Qt environment preparation and testing
- Handoff documentation for post-departure resumption
- Tag: tested-tkinter-final-20251110

### Planned - Phase 1-8 (Dec 2025 - Mar 2026)
- Complete Qt migration replacing Tkinter GUI
- Expected performance: 90-95% lag reduction
- Professional-grade multi-camera video display
- All features ported and enhanced

## [1.0.0] - 2025-10-15

### Major Release - Tkinter Version
- 8-camera synchronized capture system operational
- Master/slave architecture with control1 Pi
- 118 commits of performance optimization
- Gallery system with thumbnail generation
- Settings dialogs (camera, device naming, preferences)
- Keyboard shortcuts for rapid workflow
- Audio feedback system
- Progress indicators
- Status monitoring

### Performance Optimizations (Commits 261bf73 - a781928)
- Non-blocking network operations (61f3d2c)
- Gallery thumbnail naming fix (cdf43e8)
- IndentationError emergency fix (07e0e25)
- Canvas scrollregion debouncing (56182e2)
- Background thumbnail generation (a9720f7)
- Async file I/O for settings (b30f28e)
- Timer-based GUI updates (f43b5db, cd717ec)
- Frame rate limiting and drop logging (7669ec5, e37e3f5)
- Rep8 video freeze fix (825d202)
- Comprehensive performance instrumentation (80346eb, d54c015)

### Known Issues
- Persistent GUI lag despite optimizations (architectural Tkinter limitation)
- Cursor delay during video display (200-500ms)
- Button click delays under load
- Performance ceiling reached - no further Tkinter optimization possible

### Tags
- v1.0.0 (official release)
- tested-status-indicators-20251015-0910
- tested-progress-sync-20251014-1925
- tested-keyboard-shortcuts-20251014-1847
- tested-audio-feedback-20251014-1822
- phase-e-troubleshooting-guide-20251015

## [0.9.x] - Development Phase (2025-09-01 to 2025-10-14)

### Added
- Initial 8-camera grid layout
- Video streaming from all Raspberry Pi cameras
- Master control GUI with Tkinter
- Still capture functionality
- Gallery panel for image review
- Device naming system
- Settings persistence (JSON)
- Exclusive camera mode (single camera focus)
- Audio feedback on capture
- Keyboard shortcuts (Space, 1-8, Esc, S, G, R)
- Menu system
- Status indicators
- Heartbeat monitoring

### Changed
- Evolved from 7-camera to 8-camera system (rep1-rep8)
- Network architecture optimized for UDP video streaming
- Frame dropping strategies refined (grid vs exclusive modes)
- PhotoImage handling optimization attempts
- Event loop timing strategies

### Fixed
- Video freeze issues on rep8 after capture
- Gallery thumbnail generation blocking
- Settings dialog responsiveness
- Network command blocking
- Canvas scroll performance
- Mouse interaction tracking issues

## [0.1.x] - Initial Prototype (2025-06-01 to 2025-08-31)

### Added
- Basic Raspberry Pi camera integration
- Master/slave communication protocol
- Simple GUI for control
- Image capture functionality
- Configuration system

---

## Migration Notice

**As of 2025-11-10**: GERTIE is transitioning from Tkinter to Qt (PyQt6/PySide6) for professional-grade performance suitable for DiSSCo UK deployment (90+ institutions). This migration is necessary because:

1. **Tkinter Performance Ceiling**: After 118 optimization commits, Tkinter's single-threaded event loop cannot deliver real-time responsiveness for 8-camera video display.

2. **DiSSCo UK Requirements**: Professional-grade system needed for 10-year programme across 90+ institutions.

3. **Technical Justification**: Qt provides multi-threaded architecture (QThread), guaranteed timing (QTimer), GPU acceleration (QPixmap), and proven video application performance.

4. **Timeline**: 3-4 month migration (Dec 2025 - Mar 2026) targeting April 2026 launch.

5. **Expected Outcome**: 90-95% lag reduction, matching/exceeding commercial £15K systems.

See `STRATEGIC_PLAN_QT_MIGRATION.md` for complete migration roadmap.

---

## Version History

- **v1.0.0** (2025-10-15): Tkinter version - feature complete, performance limited
- **v2.0.0** (Planned 2026-04-01): Qt version - professional-grade performance

---

## Contributing

See `DEVELOPMENT_WORKFLOW.md` for development guidelines.
See `DEPLOYMENT_WORKFLOW.md` for deployment procedures.

---

## Contact

- Repository: https://github.com/andrc91/GERTIE-DEV
- Developer: Andrew Crane (acranephoto@gmail.com)
- Programme: DiSSCo UK Natural History Museum

---

*Changelog started: 2025-11-10*
*Last updated: 2025-11-10*
