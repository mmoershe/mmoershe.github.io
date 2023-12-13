\version "2.22.1"
\language "english"
\score
{
    % OPEN_BRACKETS:
    \context Score = "Score"
    <<
        % OPEN_BRACKETS:
        \context Staff = "RH_Staff"
        {
            % OPEN_BRACKETS:
            \context Voice = "RH_Voice"
            {
                % BEFORE:
                % COMMANDS:
                \key c \major
                % OPENING:
                % COMMANDS:
                \clef "treble"
                c''4
            % CLOSE_BRACKETS:
            }
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
}
